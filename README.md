# Extract-Shopify-Store-Product-IDs

We had a client that had a Shopify store that also signed up for some SEO work. The first thing our SEO team identified was to setup the products from the shopify store on to the primary website domain with the reasoning of having limited ability to make fundamental onsite changes to improve product discoverability. I'm not here to discuss the SEO strategy as my description may not do it justice.

While working on a method for setting up the products on the primary domain, we realized that we could use a Shopfiy JS that would render the product in the page and still give many of the common Shopfiy checkout features while keeping the checkout process themed on the domain. 

The process for generating the JS was pretty simple, basically a button click would generate a JS for teh product. However, our client has 355 products, we knew that would take forever to get into every product and copy/paste the JS and then create a new page on the domain and paste it in.

We decided to inspect the JS to see if we could determine which piece of the script contained the unique identifier for the product. THere seemed to be a couple of variables, so we tested out all of the variable combinations and we disocvered the unique combinations that worked for each product.

WIth this info in hand, we went back to the Shopify site and inspected the products to see if we could find the product variables in the code.

We knew that if we could discover the piece of script that contained the unique variables and if that data was found also in the product page code, we would be able to write a script that could output the unique ID for each product and from there it was a matter of loading the ID into the domain database to generate the script for each of the 355 products.

My technical SEO team crawled the Shopify site, provided me the URL for all of the products along with a bunch of other meta data like page title. 

I had to create a script that could crawl the HTML and isolate the product ID using CSS classes as reference points and a dictionary key-value pair to output the product ID from the HTML.

Once I had a script that could output the product ID, I tried it on a few products just to make sure there wasn't variation in how the pages were built that would give me problems. 

Once the script worked on multiple pages, I created a loop that would loop over each line in the csv in the row that contained the URL and execute the product ID extraction script for each page.

And lastly, I wrote the output to a txt file and formatted it some so it would be easy to read and verify against the xlsx from my technical SEO team.

In retrospect, I should have output to an xlsx file and formatted each row so that it would be easier for my web developer to import into the SQL database. 

I'm sure there are more efficient ways to write this script, however, I wanted to not spend more than 4h because I had assumed that's abotu how long it would have taken my SEO team to generate the same data without the script, and being a novice and having a profitability break-even point,  it took maybe 3 mins to run which is perfectly acceptiable for my parameters.

Also, as a tool, it's more important that it be practical than elegant. Elegance will come.
