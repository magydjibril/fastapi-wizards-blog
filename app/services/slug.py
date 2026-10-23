def slugify(titre: str) -> str:
    lowercase_titre = titre.lower()
    slug = lowercase_titre.replace(" ", "-")
    return slug
