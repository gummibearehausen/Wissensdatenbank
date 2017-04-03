# Wissensdatenbank

This pathon code is to derive a knowledge base from the entire Wikipedia article collection. 
running from command line: 
argument 1: wikicorpus cbor file
argument 2: name of the output knowledge base dictionary name
argument 3: name of the output knowledge base graph name
argument 4 number of wikipedia articles from corpus you would like to process. if argv[4] == null, the default is the entire wikipedia articlue collection.

pages filtered out: 
articles on category, image, template, Wikipedia: system files such as deletion, List of.., File:...


knowledge base dictionary:
1. If the entity's name is same as the surface textual form: then it is not written in the knowledge base.
2. If the surface form of the entity is different from the entity then 
      [key]:[value] = [surface form (lower case)][entity]
3. If the Wikipedia page is redirected to another entity: 
      [key]:[value] = [knowledge base entity(lower case)][redirecting entity]
