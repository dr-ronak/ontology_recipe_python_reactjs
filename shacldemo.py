import pyshacl

shapes_graph = """
@prefix dash: <http://datashapes.org/dash#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix schema: <http://schema.org/> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

schema:PersonShape
    a sh:NodeShape ;
    sh:targetClass schema:Person ;
    sh:property [
        sh:path schema:givenName ;
        sh:datatype xsd:string ;
        sh:name "given name" ;
    ] ;    
    sh:property [
        sh:path schema:age ;
        sh:node schema:AgeShape ;
        sh:datatype xsd:integer ;
        sh:minInclusive 1 ;
        sh:maxInclusive 100 ;
    ] .
"""

data_graph = """
{
    "@context": { "@vocab": "http://schema.org/" },

    "@id": "http://example.org/ns#Bob",
    "@type": "Person",
    "givenName": "Robert",
    "familyName": "Junior",
    "age": -5
}
"""

results = pyshacl.validate(
    data_graph,
    shacl_graph=shapes_graph,
    data_graph_format="json-ld",
    shacl_graph_format="ttl",
    inference="rdfs",
    debug=True,
    serialize_report_graph="ttl",
    )

conforms, report_graph, report_text = results

print("conforms", conforms)
print(report_text)