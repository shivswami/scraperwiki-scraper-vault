# encoding: utf-8

# Trovit.co.uk premium property ads dataminer

require 'open-uri'
require 'nokogiri'
queries=[
"type.1/what_d.London",
"type.1/what_d.Birmingham",
"type.1/what_d.Leeds",
"type.1/what_d.Glasgow",
"type.1/what_d.Sheffield",
"type.1/what_d.Bradford",
"type.1/what_d.Edinburgh",
"type.1/what_d.Liverpool",
"type.1/what_d.Manchester",
"type.1/what_d.Bristol",
"type.1/what_d.Wakefield",
"type.1/what_d.Cardiff",
"type.1/what_d.Coventry",
"type.1/what_d.Nottingham",
"type.1/what_d.Leicester",
"type.1/what_d.Sunderland",
"type.1/what_d.Belfast",
"type.1/what_d.Newcastle upon Tyne",
"type.1/what_d.Brighton",
"type.1/what_d.Hull",
"type.1/what_d.Plymouth",
"type.1/what_d.Stoke-on-Trent",
"type.1/what_d.Wolverhampton",
"type.1/what_d.Derby",
"type.1/what_d.Swansea",
"type.1/what_d.Southampton",
"type.1/what_d.Salford",
"type.1/what_d.Aberdeen",
"type.1/what_d.Westminster",
"type.1/what_d.Portsmouth",
"type.1/what_d.York",
"type.1/what_d.Peterborough",
"type.1/what_d.Dundee",
"type.1/what_d.Lancaster",
"type.1/what_d.Oxford",
"type.1/what_d.Newport",
"type.1/what_d.Preston",
"type.1/what_d.St Albans",
"type.1/what_d.Norwich",
"type.1/what_d.Chester",
"type.1/what_d.Cambridge",
"type.1/what_d.Salisbury",
"type.1/what_d.Exeter",
"type.1/what_d.Gloucester",
"type.1/what_d.Lisburn",
"type.1/what_d.Chichester",
"type.1/what_d.Winchester",
"type.1/what_d.Londonderry",
"type.1/what_d.Carlisle",
"type.1/what_d.Worcester",
"type.1/what_d.Bath",
"type.1/what_d.Durham",
"type.1/what_d.Lincoln",
"type.1/what_d.Hereford",
"type.1/what_d.Armagh",
"type.1/what_d.Inverness",
"type.1/what_d.Stirling",
"type.1/what_d.Canterbury",
"type.1/what_d.Lichfield",
"type.1/what_d.Newry",
"type.1/what_d.Ripon",
"type.1/what_d.Bangor",
"type.1/what_d.Truro",
"type.1/what_d.Ely",
"type.1/what_d.Wells",
"type.1/what_d.St Davids",
"type.2/what_d.London",
"type.2/what_d.Birmingham",
"type.2/what_d.Leeds",
"type.2/what_d.Glasgow",
"type.2/what_d.Sheffield",
"type.2/what_d.Bradford",
"type.2/what_d.Edinburgh",
"type.2/what_d.Liverpool",
"type.2/what_d.Manchester",
"type.2/what_d.Bristol",
"type.2/what_d.Wakefield",
"type.2/what_d.Cardiff",
"type.2/what_d.Coventry",
"type.2/what_d.Nottingham",
"type.2/what_d.Leicester",
"type.2/what_d.Sunderland",
"type.2/what_d.Belfast",
"type.2/what_d.Newcastle upon Tyne",
"type.2/what_d.Brighton",
"type.2/what_d.Hull",
"type.2/what_d.Plymouth",
"type.2/what_d.Stoke-on-Trent",
"type.2/what_d.Wolverhampton",
"type.2/what_d.Derby",
"type.2/what_d.Swansea",
"type.2/what_d.Southampton",
"type.2/what_d.Salford",
"type.2/what_d.Aberdeen",
"type.2/what_d.Westminster",
"type.2/what_d.Portsmouth",
"type.2/what_d.York",
"type.2/what_d.Peterborough",
"type.2/what_d.Dundee",
"type.2/what_d.Lancaster",
"type.2/what_d.Oxford",
"type.2/what_d.Newport",
"type.2/what_d.Preston",
"type.2/what_d.St Albans",
"type.2/what_d.Norwich",
"type.2/what_d.Chester",
"type.2/what_d.Cambridge",
"type.2/what_d.Salisbury",
"type.2/what_d.Exeter",
"type.2/what_d.Gloucester",
"type.2/what_d.Lisburn",
"type.2/what_d.Chichester",
"type.2/what_d.Winchester",
"type.2/what_d.Londonderry",
"type.2/what_d.Carlisle",
"type.2/what_d.Worcester",
"type.2/what_d.Bath",
"type.2/what_d.Durham",
"type.2/what_d.Lincoln",
"type.2/what_d.Hereford",
"type.2/what_d.Armagh",
"type.2/what_d.Inverness",
"type.2/what_d.Stirling",
"type.2/what_d.Canterbury",
"type.2/what_d.Lichfield",
"type.2/what_d.Newry",
"type.2/what_d.Ripon",
"type.2/what_d.Bangor",
"type.2/what_d.Truro",
"type.2/what_d.Ely",
"type.2/what_d.Wells",
"type.2/what_d.St Davids",
"type.3/what_d.London",
"type.3/what_d.Birmingham",
"type.3/what_d.Leeds",
"type.3/what_d.Glasgow",
"type.3/what_d.Sheffield",
"type.3/what_d.Bradford",
"type.3/what_d.Edinburgh",
"type.3/what_d.Liverpool",
"type.3/what_d.Manchester",
"type.3/what_d.Bristol",
"type.3/what_d.Wakefield",
"type.3/what_d.Cardiff",
"type.3/what_d.Coventry",
"type.3/what_d.Nottingham",
"type.3/what_d.Leicester",
"type.3/what_d.Sunderland",
"type.3/what_d.Belfast",
"type.3/what_d.Newcastle upon Tyne",
"type.3/what_d.Brighton",
"type.3/what_d.Hull",
"type.3/what_d.Plymouth",
"type.3/what_d.Stoke-on-Trent",
"type.3/what_d.Wolverhampton",
"type.3/what_d.Derby",
"type.3/what_d.Swansea",
"type.3/what_d.Southampton",
"type.3/what_d.Salford",
"type.3/what_d.Aberdeen",
"type.3/what_d.Westminster",
"type.3/what_d.Portsmouth",
"type.3/what_d.York",
"type.3/what_d.Peterborough",
"type.3/what_d.Dundee",
"type.3/what_d.Lancaster",
"type.3/what_d.Oxford",
"type.3/what_d.Newport",
"type.3/what_d.Preston",
"type.3/what_d.St Albans",
"type.3/what_d.Norwich",
"type.3/what_d.Chester",
"type.3/what_d.Cambridge",
"type.3/what_d.Salisbury",
"type.3/what_d.Exeter",
"type.3/what_d.Gloucester",
"type.3/what_d.Lisburn",
"type.3/what_d.Chichester",
"type.3/what_d.Winchester",
"type.3/what_d.Londonderry",
"type.3/what_d.Carlisle",
"type.3/what_d.Worcester",
"type.3/what_d.Bath",
"type.3/what_d.Durham",
"type.3/what_d.Lincoln",
"type.3/what_d.Hereford",
"type.3/what_d.Armagh",
"type.3/what_d.Inverness",
"type.3/what_d.Stirling",
"type.3/what_d.Canterbury",
"type.3/what_d.Newry",
"type.3/what_d.Ripon",
"type.3/what_d.Bangor",
"type.3/what_d.Truro",
"type.3/what_d.Ely",
"type.3/what_d.Wells",
"type.3/what_d.St Davids"
]
counts = Hash.new(0)
j=0
while j<queries.count
  queryurl='http://homes.trovit.co.uk/index.php/cod.search_homes/'+queries[j]
 # puts queryurl
  doc = Nokogiri::HTML(open(URI::encode(queryurl)))
doc.search("div[@id='wrapper_ppc_top']").each do |node|
 innode=node.search("p[@class='description']")
    cells=innode.search("small")  
    if(cells.count>0)  
    #puts cells.text
    name=cells.text
    data={
         advertiser: name,
         occurrences: counts[name] += 1
    }
          ScraperWiki::save_sqlite(['advertiser'], data)
   end
end
doc.search("div[@id='wrapper_ppc_bottom']").each do |node|
 innode=node.search("p[@class='description']")
    cells=innode.search("small")   
   # puts cells.text
    if(cells.count>0)  
   name=cells.text
   data={
         advertiser: name,
         occurrences: counts[name] += 1
    }
          ScraperWiki::save_sqlite(['advertiser'], data)
  end
  end
j=j+1
end
# encoding: utf-8

# Trovit.co.uk premium property ads dataminer

require 'open-uri'
require 'nokogiri'
queries=[
"type.1/what_d.London",
"type.1/what_d.Birmingham",
"type.1/what_d.Leeds",
"type.1/what_d.Glasgow",
"type.1/what_d.Sheffield",
"type.1/what_d.Bradford",
"type.1/what_d.Edinburgh",
"type.1/what_d.Liverpool",
"type.1/what_d.Manchester",
"type.1/what_d.Bristol",
"type.1/what_d.Wakefield",
"type.1/what_d.Cardiff",
"type.1/what_d.Coventry",
"type.1/what_d.Nottingham",
"type.1/what_d.Leicester",
"type.1/what_d.Sunderland",
"type.1/what_d.Belfast",
"type.1/what_d.Newcastle upon Tyne",
"type.1/what_d.Brighton",
"type.1/what_d.Hull",
"type.1/what_d.Plymouth",
"type.1/what_d.Stoke-on-Trent",
"type.1/what_d.Wolverhampton",
"type.1/what_d.Derby",
"type.1/what_d.Swansea",
"type.1/what_d.Southampton",
"type.1/what_d.Salford",
"type.1/what_d.Aberdeen",
"type.1/what_d.Westminster",
"type.1/what_d.Portsmouth",
"type.1/what_d.York",
"type.1/what_d.Peterborough",
"type.1/what_d.Dundee",
"type.1/what_d.Lancaster",
"type.1/what_d.Oxford",
"type.1/what_d.Newport",
"type.1/what_d.Preston",
"type.1/what_d.St Albans",
"type.1/what_d.Norwich",
"type.1/what_d.Chester",
"type.1/what_d.Cambridge",
"type.1/what_d.Salisbury",
"type.1/what_d.Exeter",
"type.1/what_d.Gloucester",
"type.1/what_d.Lisburn",
"type.1/what_d.Chichester",
"type.1/what_d.Winchester",
"type.1/what_d.Londonderry",
"type.1/what_d.Carlisle",
"type.1/what_d.Worcester",
"type.1/what_d.Bath",
"type.1/what_d.Durham",
"type.1/what_d.Lincoln",
"type.1/what_d.Hereford",
"type.1/what_d.Armagh",
"type.1/what_d.Inverness",
"type.1/what_d.Stirling",
"type.1/what_d.Canterbury",
"type.1/what_d.Lichfield",
"type.1/what_d.Newry",
"type.1/what_d.Ripon",
"type.1/what_d.Bangor",
"type.1/what_d.Truro",
"type.1/what_d.Ely",
"type.1/what_d.Wells",
"type.1/what_d.St Davids",
"type.2/what_d.London",
"type.2/what_d.Birmingham",
"type.2/what_d.Leeds",
"type.2/what_d.Glasgow",
"type.2/what_d.Sheffield",
"type.2/what_d.Bradford",
"type.2/what_d.Edinburgh",
"type.2/what_d.Liverpool",
"type.2/what_d.Manchester",
"type.2/what_d.Bristol",
"type.2/what_d.Wakefield",
"type.2/what_d.Cardiff",
"type.2/what_d.Coventry",
"type.2/what_d.Nottingham",
"type.2/what_d.Leicester",
"type.2/what_d.Sunderland",
"type.2/what_d.Belfast",
"type.2/what_d.Newcastle upon Tyne",
"type.2/what_d.Brighton",
"type.2/what_d.Hull",
"type.2/what_d.Plymouth",
"type.2/what_d.Stoke-on-Trent",
"type.2/what_d.Wolverhampton",
"type.2/what_d.Derby",
"type.2/what_d.Swansea",
"type.2/what_d.Southampton",
"type.2/what_d.Salford",
"type.2/what_d.Aberdeen",
"type.2/what_d.Westminster",
"type.2/what_d.Portsmouth",
"type.2/what_d.York",
"type.2/what_d.Peterborough",
"type.2/what_d.Dundee",
"type.2/what_d.Lancaster",
"type.2/what_d.Oxford",
"type.2/what_d.Newport",
"type.2/what_d.Preston",
"type.2/what_d.St Albans",
"type.2/what_d.Norwich",
"type.2/what_d.Chester",
"type.2/what_d.Cambridge",
"type.2/what_d.Salisbury",
"type.2/what_d.Exeter",
"type.2/what_d.Gloucester",
"type.2/what_d.Lisburn",
"type.2/what_d.Chichester",
"type.2/what_d.Winchester",
"type.2/what_d.Londonderry",
"type.2/what_d.Carlisle",
"type.2/what_d.Worcester",
"type.2/what_d.Bath",
"type.2/what_d.Durham",
"type.2/what_d.Lincoln",
"type.2/what_d.Hereford",
"type.2/what_d.Armagh",
"type.2/what_d.Inverness",
"type.2/what_d.Stirling",
"type.2/what_d.Canterbury",
"type.2/what_d.Lichfield",
"type.2/what_d.Newry",
"type.2/what_d.Ripon",
"type.2/what_d.Bangor",
"type.2/what_d.Truro",
"type.2/what_d.Ely",
"type.2/what_d.Wells",
"type.2/what_d.St Davids",
"type.3/what_d.London",
"type.3/what_d.Birmingham",
"type.3/what_d.Leeds",
"type.3/what_d.Glasgow",
"type.3/what_d.Sheffield",
"type.3/what_d.Bradford",
"type.3/what_d.Edinburgh",
"type.3/what_d.Liverpool",
"type.3/what_d.Manchester",
"type.3/what_d.Bristol",
"type.3/what_d.Wakefield",
"type.3/what_d.Cardiff",
"type.3/what_d.Coventry",
"type.3/what_d.Nottingham",
"type.3/what_d.Leicester",
"type.3/what_d.Sunderland",
"type.3/what_d.Belfast",
"type.3/what_d.Newcastle upon Tyne",
"type.3/what_d.Brighton",
"type.3/what_d.Hull",
"type.3/what_d.Plymouth",
"type.3/what_d.Stoke-on-Trent",
"type.3/what_d.Wolverhampton",
"type.3/what_d.Derby",
"type.3/what_d.Swansea",
"type.3/what_d.Southampton",
"type.3/what_d.Salford",
"type.3/what_d.Aberdeen",
"type.3/what_d.Westminster",
"type.3/what_d.Portsmouth",
"type.3/what_d.York",
"type.3/what_d.Peterborough",
"type.3/what_d.Dundee",
"type.3/what_d.Lancaster",
"type.3/what_d.Oxford",
"type.3/what_d.Newport",
"type.3/what_d.Preston",
"type.3/what_d.St Albans",
"type.3/what_d.Norwich",
"type.3/what_d.Chester",
"type.3/what_d.Cambridge",
"type.3/what_d.Salisbury",
"type.3/what_d.Exeter",
"type.3/what_d.Gloucester",
"type.3/what_d.Lisburn",
"type.3/what_d.Chichester",
"type.3/what_d.Winchester",
"type.3/what_d.Londonderry",
"type.3/what_d.Carlisle",
"type.3/what_d.Worcester",
"type.3/what_d.Bath",
"type.3/what_d.Durham",
"type.3/what_d.Lincoln",
"type.3/what_d.Hereford",
"type.3/what_d.Armagh",
"type.3/what_d.Inverness",
"type.3/what_d.Stirling",
"type.3/what_d.Canterbury",
"type.3/what_d.Newry",
"type.3/what_d.Ripon",
"type.3/what_d.Bangor",
"type.3/what_d.Truro",
"type.3/what_d.Ely",
"type.3/what_d.Wells",
"type.3/what_d.St Davids"
]
counts = Hash.new(0)
j=0
while j<queries.count
  queryurl='http://homes.trovit.co.uk/index.php/cod.search_homes/'+queries[j]
 # puts queryurl
  doc = Nokogiri::HTML(open(URI::encode(queryurl)))
doc.search("div[@id='wrapper_ppc_top']").each do |node|
 innode=node.search("p[@class='description']")
    cells=innode.search("small")  
    if(cells.count>0)  
    #puts cells.text
    name=cells.text
    data={
         advertiser: name,
         occurrences: counts[name] += 1
    }
          ScraperWiki::save_sqlite(['advertiser'], data)
   end
end
doc.search("div[@id='wrapper_ppc_bottom']").each do |node|
 innode=node.search("p[@class='description']")
    cells=innode.search("small")   
   # puts cells.text
    if(cells.count>0)  
   name=cells.text
   data={
         advertiser: name,
         occurrences: counts[name] += 1
    }
          ScraperWiki::save_sqlite(['advertiser'], data)
  end
  end
j=j+1
end
