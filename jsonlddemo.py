from pyld import jsonld
import json

doc = {
    "http://schema.org/name": "Dr. Ronak Panchal",
    "http://schema.org/email": "ronu27@gmail.com",
    "http://schema.org/telephone": "+919898257016",
    "http://schema.org/url": {"@id": "https://drronakpanchal.wordpress.com/"},
    "http://schema.org/image": {"@id": "https://drronakpanchal.files.wordpress.com/2020/12/mic-with.jpeg"},
    "http://schema.org/ingredient":[{"@id":"http://www.recipe.com/ontology#Almond"},{"@id":"http://www.recipe.com/ontology#Ginger"}]
}

context = {
    "name": "http://schema.org/name",
    "email": "http://schema.org/email",
    "telephone": "http://schema.org/telephone",
    "homepage": {"@id": "http://schema.org/url", "@type": "@id"},
    "image": {"@id": "http://schema.org/image", "@type": "@id"},
    "ingredient": {"@id":"http://schema.org/ingredient"}
}

# compact a document according to a particular context
# see: https://json-ld.org/spec/latest/json-ld/#compacted-document-form
compacted = jsonld.compact(doc, context)

print(json.dumps(compacted, indent=2))
# Output:
# {
#   "@context": {...},
#   "image": "http://manu.sporny.org/images/manu.png",
#   "homepage": "http://manu.sporny.org/",
#   "name": "Manu Sporny"
# }

