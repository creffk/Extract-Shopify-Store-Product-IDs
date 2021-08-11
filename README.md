# Extract-Shopify-Store-Product-IDs

We had a client that had a Shopify store that also signed up for some SEO work. The first thing our SEO team identified was to setup the products from the shopify store on to the primary website domain with the reasoning of having limited ability to make fundamental onsite changes to improve product discoverability. I'm not here to discuss the SEO strategy as my description may not do it justice.

While working on a method for setting up the products on the primary domain, we realized that we could use a Shopfiy JS that would render the product in the page and still give many of the common Shopfiy checkout features while keeping the checkout process themed on the domain. 

The process for generating the JS was pretty simple, basically a button click would generate a JS for the product. However, our client has 355 products, we knew that would take forever to get into every product and copy/paste the JS and then create a new page on the domain and paste it in.

We decided to inspect the JS to see if we could determine which piece of the script contained the unique identifier for the product. There seemed to be a couple of variables, so we tested out all of the variable combinations and we disocvered the unique combinations that worked for each product.

With this info in hand, we went back to the Shopify site and inspected the products to see if we could find the product variables in the code.

We knew that if we could discover the piece of script that contained the unique variables and if that data was found also in the product page code, we would be able to write a script that could output the unique ID for each product and from there it was a matter of loading the ID into the domain database to generate the script for each of the 355 products.

My technical SEO team crawled the Shopify site, provided me the URL for all of the products along with a bunch of other meta data like page title. 

I had to create a script that could crawl the HTML and isolate the product ID using a tag and CSS classes as reference points to output the product ID from the HTML.

Once I had a script that could output the product ID, I tried it on a few products just to make sure there wasn't page-to-page variation in how the pages were structured that would give me problems using the chosen tag and css class.

Once the script worked on multiple pages, I created a loop that would loop over each line in the csv in the row that contained the URL and execute the product ID extraction script for each page.

And lastly, I wrote the output to a txt file and formatted it some so it would be easy to read and verify against the xlsx from my technical SEO team.

Once I had my output file, I passed it over to my web develoment team to make a new custom post type that had the script built into the page template so when we import the product ID into the SQL database as a custom field, the page would render the content and it would be editable from the admin of the site.

In retrospect, I should have output to an xlsx file and formatted each row so that it would be easier for my web developer to import into the SQL database. Also, this method doesn't replace a standard shopping cart. Setting up the pages so that only the product ID is in the database means we can't efficiently setup a standard shop/catalog page with thumbnails that the user can use to browse the site and easily choose between similar products. I'll update this when we have decided on a solution to this issue.

I'm sure there are more efficient ways to write this script, however, I wanted to not spend more than 4h. I knew that if it took longer to develop a script to complete this task manually, the script would not be doing it's. After all, it took maybe 3 mins to run. 
