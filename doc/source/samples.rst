Some sample examples
####################

Here are some samples for using CouchDB Views.

To get the whole list of all documents, just call the `_all_docs` view. It's provided by 
default by CouchDB::

    GET http://localhost:5984/dropit/_all_docs
    
    {"total_rows":6,"offset":0,"rows":[
    {"id":"2-ice-creams","key":"2-ice-creams","value":{"rev":"6-fb75a0ebd1dae0d76fe404dd333e3db6"}},
    {"id":"2-monkey-monkey","key":"2-monkey-monkey","value":{"rev":"3-5c61be897d6a0fe7fdacc770890a095a"}},
    {"id":"3-monkey-monkey","key":"3-monkey-monkey","value":{"rev":"4-d278facfc6f4363071acd134fdddc879"}},
    {"id":"_design/notes","key":"_design/notes","value":{"rev":"23-b96882bc82b5a22a8a5a56bed2c5ff8d"}},
    {"id":"ice-creams","key":"ice-creams","value":{"rev":"3-b189d414be65105d65d637dcdb152a11"}},
    {"id":"monkey-monkey","key":"monkey-monkey","value":{"rev":"3-3006820a8ae62043bbd7ebc626ff6f9b"}}
    ]}

Notes
=====

To get the history of revisions, by root note (here, "monkey-monkey")::

    GET http://localhost:5984/dropit/_design/notes/_view/history?startkey=[%22monkey-monkey%22]&endkey=[%22monkey-monkey%22,[]]
    
    {"total_rows":3,"offset":1,"rows":[
    {"id":"2-monkey-monkey","key":["monkey-monkey","2-monkey-monkey"],"value":{"_id":"2-monkey-monkey","_rev":"5-29c5eb6185a3ea466dd7f0e706e72520","title":"Monkey, Monkey, Monkeys !!!!!","tags":["hey","monkeys","are","funny"],"content":"According to the Oxford English Dictionary, the word monkey may originate in a German version of the Reynard the Fox fable, published circa 1580. In this version of the fable, a character named Moneke is the son of Martin the Ape. The word Moneke may have been derived from the Italian monna, which means 'a female ape'. The name Moneke likely persisted over time due to the popularity of Reynard the Fox.  The term 'monkey' is an artificial grouping; it is not a 'good' taxon, but instead it is a paraphyletic group, like 'fish'. A 'good' taxon, as most modern biologists consider it, is a monophyletic group, that is, a group consisting of all the evolutionary descendants of a single ancestor species. The term 'monkey' covers all platyrrhines (flat, broad noses) and some catarrhines (nostrils-downwards), but excludes the apes.[1]  Due to its size (up to 1 m/3 ft) the Mandrill is often thought to be an ape, but it is actually an Old World monkey. Also, a few monkey species deceptively have the word 'ape' in their common name, such as the Barbary Ape.  A group of monkeys may be referred to as a mission or a tribe.","doc_type":"http://dropit.notmyidea.org/note","rev_number":2,"is_head":false,"root_note":"monkey-monkey"}},
    {"id":"monkey-monkey","key":["monkey-monkey","monkey-monkey"],"value":{"_id":"monkey-monkey","_rev":"3-3006820a8ae62043bbd7ebc626ff6f9b","title":"Monkey, Monkey !","tags":["hey","monkeys","are","funny"],"content":"According to the Oxford English Dictionary, the word monkey may originate in a German version of the Reynard the Fox fable, published circa 1580. In this version of the fable, a character named Moneke is the son of Martin the Ape. The word Moneke may have been derived from the Italian monna, which means 'a female ape'. The name Moneke likely persisted over time due to the popularity of Reynard the Fox.  The term 'monkey' is an artificial grouping; it is not a 'good' taxon, but instead it is a paraphyletic group, like 'fish'. A 'good' taxon, as most modern biologists consider it, is a monophyletic group, that is, a group consisting of all the evolutionary descendants of a single ancestor species. The term 'monkey' covers all platyrrhines (flat, broad noses) and some catarrhines (nostrils-downwards), but excludes the apes.[1]  Due to its size (up to 1 m/3 ft) the Mandrill is often thought to be an ape, but it is actually an Old World monkey. Also, a few monkey species deceptively have the word 'ape' in their common name, such as the Barbary Ape.  A group of monkeys may be referred to as a mission or a tribe.","doc_type":"http://dropit.notmyidea.org/note","rev_nuber":1,"is_head":false}}

To get the last heads, use the `head` view ::

    GET http://localhost:5984/dropit/_design/notes/_view/heads
    {"total_rows":2,"offset":0,"rows":[
    {"id":"2-ice-creams","key":"2-ice-creams","value":{"_id":"2-ice-creams","_rev":"7-fa62759588e0e0fa96e9b1d0ee1d5c12","title":"Ice creams (again) !","tags":["love","alice","icecreams","funny"],"content":"The meaning of the term ice cream varies from one country to another. Terms like frozen custard, frozen yogurt, sorbet, gelato and others are used to distinguish different varieties and styles. In some countries, like the USA, the term ice cream applies only to a specific variety, and their governments regulate the commercial use of all these terms based on quantities of ingredients.[2] In others, like Italy and Argentina, one word is used for all the variants. Alternatives made from soy milk, rice milk, and goat milk are available for those who are lactose intolerant or have an allergy to dairy protein, or in the case of soy and rice milk, for those who want to avoid animal products.","doc_type":"http://dropit.notmyidea.org/note","rev_number":2,"is_head":true,"root_note":"ice-creams"}},
    {"id":"3-monkey-monkey","key":"3-monkey-monkey","value":{"_id":"3-monkey-monkey","_rev":"5-8523017cefd1ac2a8accd5b81cc6a61d","title":"Monkeys again !","tags":["hey","monkeys","are","funny"],"content":"According to the Oxford English Dictionary, the word monkey may originate in a German version of the Reynard the Fox fable, published circa 1580. In this version of the fable, a character named Moneke is the son of Martin the Ape. The word Moneke may have been derived from the Italian monna, which means 'a female ape'. The name Moneke likely persisted over time due to the popularity of Reynard the Fox.  The term 'monkey' is an artificial grouping; it is not a 'good' taxon, but instead it is a paraphyletic group, like 'fish'. A 'good' taxon, as most modern biologists consider it, is a monophyletic group, that is, a group consisting of all the evolutionary descendants of a single ancestor species. The term 'monkey' covers all platyrrhines (flat, broad noses) and some catarrhines (nostrils-downwards), but excludes the apes.[1]  Due to its size (up to 1 m/3 ft) the Mandrill is often thought to be an ape, but it is actually an Old World monkey. Also, a few monkey species deceptively have the word 'ape' in their common name, such as the Barbary Ape.  A group of monkeys may be referred to as a mission or a tribe.","doc_type":"http://dropit.notmyidea.org/note","rev_number":3,"is_head":true,"root_note":"monkey-monkey"}}
    ]}

You can also get a summary of all notes ::

    GET http://localhost:5984/dropit/_design/notes/_view/summary
    {"total_rows":5,"offset":0,"rows":[
    {"id":"2-ice-creams","key":"2-ice-creams","value":{"title":"Ice creams (again) !","tags":["love","alice","icecreams","funny"],"summary":"The meaning of the term ice cream varies from one country to another. Terms like frozen custard, frozen yogurt, sorbet, gelato and others ar"}},
    {"id":"2-monkey-monkey","key":"2-monkey-monkey","value":{"title":"Monkey, Monkey, Monkeys !!!!!","tags":["hey","monkeys","are","funny"],"summary":"According to the Oxford English Dictionary, the word monkey may originate in a German version of the Reynard the Fox fable, published circa "}},
    {"id":"3-monkey-monkey","key":"3-monkey-monkey","value":{"title":"Monkeys again !","tags":["hey","monkeys","are","funny"],"summary":"According to the Oxford English Dictionary, the word monkey may originate in a German version of the Reynard the Fox fable, published circa "}},
    {"id":"ice-creams","key":"ice-creams","value":{"title":"Ice creams !","tags":["love","alice","icecreams","funny"],"summary":"The meaning of the term ice cream varies from one country to another. Terms like frozen custard, frozen yogurt, sorbet, gelato and others ar"}},
    {"id":"monkey-monkey","key":"monkey-monkey","value":{"title":"Monkey, Monkey !","tags":["hey","monkeys","are","funny"],"summary":"According to the Oxford English Dictionary, the word monkey may originate in a German version of the Reynard the Fox fable, published circa "}}
    ]}

Tags
=====

To get the whole list of tags, use the `tags` view. Here we pass in the reduce 
function. So we get the list of tags and a coefficient::

    GET "http://localhost:5984/dropit/_design/notes/_view/tags?group=true"
    
    {"rows":[
    {"key":"alice","value":1},
    {"key":"are","value":1},
    {"key":"funny","value":2},
    {"key":"hey","value":1},
    {"key":"icecreams","value":1},
    {"key":"love","value":1},
    {"key":"monkeys","value":1}
    ]}

If we just want the list of tags, without reduce function:: 
     
    GET "http://localhost:5984/dropit/_design/notes/_view/tags?reduce=false"
    
    {"total_rows":8,"offset":0,"rows":[
    {"id":"2-ice-creams","key":"alice","value":1},
    {"id":"3-monkey-monkey","key":"are","value":1},
    {"id":"2-ice-creams","key":"funny","value":1},
    {"id":"3-monkey-monkey","key":"funny","value":1},
    {"id":"3-monkey-monkey","key":"hey","value":1},
    {"id":"2-ice-creams","key":"icecreams","value":1},
    {"id":"2-ice-creams","key":"love","value":1},
    {"id":"3-monkey-monkey","key":"monkeys","value":1}
    ]}

For viewing a list of documents, by tags, we can access the couchdb view named 
`by_tag` by http:: 
    
    GET "http://localhost:5984/dropit/_design/notes/_view/by_tag"

    ... (stripped)

For instance, using curl, we can retreive all the documents tagged with "funny"::

    GET "http://localhost:5984/dropit/_design/notes/_view/by_tag?startkey=%22funny%22&endkey=%22funny%22"

    {"total_rows":8,"offset":2,"rows":[
    {"id":"2-ice-creams","key":"funny","value":{"_id":"2-ice-creams","_rev":"6-fb75a0ebd1dae0d76fe404dd333e3db6","title":"Ice creams (again) !","tags":["love","alice","icecreams","funny"],"content":"The meaning of the term ice cream varies from one country to another. Terms like frozen custard, frozen yogurt, sorbet, gelato and others are used to distinguish different varieties and styles. In some countries, like the USA, the term ice cream applies only to a specific variety, and their governments regulate the commercial use of all these terms based on quantities of ingredients.[2] In others, like Italy and Argentina, one word is used for all the variants. Alternatives made from soy milk, rice milk, and goat milk are available for those who are lactose intolerant or have an allergy to dairy protein, or in the case of soy and rice milk, for those who want to avoid animal products.","doc_type":"http://dropit.notmyidea.org/note","parent_note":"ice-creams","rev_number":2,"is_head":true}},
    {"id":"3-monkey-monkey","key":"funny","value":{"_id":"3-monkey-monkey","_rev":"4-d278facfc6f4363071acd134fdddc879","title":"Monkeys again !","tags":["hey","monkeys","are","funny"],"content":"According to the Oxford English Dictionary, the word monkey may originate in a German version of the Reynard the Fox fable, published circa 1580. In this version of the fable, a character named Moneke is the son of Martin the Ape. The word Moneke may have been derived from the Italian monna, which means 'a female ape'. The name Moneke likely persisted over time due to the popularity of Reynard the Fox.  The term 'monkey' is an artificial grouping; it is not a 'good' taxon, but instead it is a paraphyletic group, like 'fish'. A 'good' taxon, as most modern biologists consider it, is a monophyletic group, that is, a group consisting of all the evolutionary descendants of a single ancestor species. The term 'monkey' covers all platyrrhines (flat, broad noses) and some catarrhines (nostrils-downwards), but excludes the apes.[1]  Due to its size (up to 1 m/3 ft) the Mandrill is often thought to be an ape, but it is actually an Old World monkey. Also, a few monkey species deceptively have the word 'ape' in their common name, such as the Barbary Ape.  A group of monkeys may be referred to as a mission or a tribe.","doc_type":"http://dropit.notmyidea.org/note","parent_note":"monkey-monkey","rev_number":3,"is_head":true}}
    ]}


