from googlesearch import search

class LinkedInSearchQueryBuilder:
    def __init__(self, company, position, role_type=None, location=None, school=None):
        self.company = company
        self.position = position
        self.role_type = role_type
        self.location = location
        self.school = school
        self.extra_keywords = []

        self.role_map = {
            "PM": ["product manager", "project manager"],
            "Recruiter": ["recruiter"],
            "CEO": ["ceo"],
            "HR": ["human resources", "hr"]
        }

    def add_keyword(self, keyword):
        """Add extra key words（eg. school, industry）"""
        self.extra_keywords.append(keyword)
    
    def or_group(self, role_keywords):
        """Convert ['a', 'b'] -> ("a" OR "b") role_map"""
        if not role_keywords:
            return ""
        return "(" + " OR ".join(f'"{kw}"' for kw in role_keywords) + ")"

    def build_query(self):

        role_keywords = self.role_map.get(self.role_type, [self.role_type]) # map the dict, if not match -> use the input from user
        or_role = self.or_group(role_keywords)

        base_keywords = [self.company, self.position, or_role, self.location, self.school] + self.extra_keywords
        keyword_part = " ".join(f'"{kw}"' for kw in base_keywords if kw) # "kw" if kw is not None
        
        return f'site:linkedin.com/in OR site:linkedin.com/pub {keyword_part}'

    def search(self, limit=5):
        query = self.build_query()
        print(f"[DEBUG] Google Query: {query}")
        return list(search(query, num_results=limit))
    
    def get_query_and_limit(self, limit):
        return self.build_query(), limit

# Test
if __name__ == "__main__":
    searcher = LinkedInSearchQueryBuilder(
        company="google",
        position="software engineer",
        location="new york",
        role_type="PM",
        school = "Queens college"
    )

    # searcher.add_keyword("Columbia University")  # Add school
    # qyery_line, limit = searcher.get_query_and_limit(limit=6)

    results = searcher.search(limit = 6)

    print("\n🔗 LinkedIn Results:")
    for url in results:
        print(url)
