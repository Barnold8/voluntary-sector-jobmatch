# Email -> Ideas

## Statement

This is an overview of the requirements E-Mail. The contents are similar but are not 1:1. This is because no consent was given for data collection from the stakeholder. This is just going to be some points and idea jotting to help me gather an idea on what can be done to help the stakeholder. This file is going to be more of a stream of consciousness than an actual revised document. To see a revised document on the findings here and findings externally, look at [findings.tex](findings.tex)

## Raw filtered email

    I want to prepare a database that can deliver a VOLUNTARY SECTOR JOB MATCH .

    I may mean VOLUNTARY SECTOR SKILLS match

    There is also an element of CAREER DEVELOPMENT in the **REDACTED** voluntary sector

    I don’t know what there is nationally of a similar offer.

    I wish to avoid GDPR issues with information we hold or share

    I need people to register to use the service , and have a charge for users to generate income for its management.

    It will need to describe knowledge areas, skills, previous or type of project/ work done and seeking as well as work areas considered .

    It could also have  a “ jobs available “ / skills Im looking for section

    Id like to have a reporting facility to check number of users  

## What volunteering services and companies already exist and how are they operating?
    
    This question is asked to gain some better understanding on how charities operate and what might be the most cost effective strategies. 

### [Reach volunteering](https://reachvolunteering.org.uk/)

This one is like a megaphone for smaller charities. Reach facilitates charities and organisations to post volunteering roles to the site directly for [free, (most of the time),](https://reachvolunteering.org.uk/posting-opportunity#:~:text=Reach%20Volunteering%E2%80%99s%20services,charge%20for%20volunteers) due to their funding. One major flaw of Reach is the minimum requirements for a volunteer posting, specifically the [experience required](https://reachvolunteering.org.uk/our-criteria-opportunities#:~:text=require%20three%20or%20more%20years%20professional%20experience%20in%C2%A0one%20of%20our%20skills%20areas). Reach requirees a poosting require 3 years _minimum_ for a role which defeats the point of volunteering almost entirely. 


<h4>Pros: </h4>

- Works alongside other volunteering charities to post volunteering advertisements
- Most of the time it is free to post an advertisement
- Due to the requirements for a volunteer post, its highly unlikely spam will get through

<h4>Cons: </h4>

- Limited on what volunteering roles can be posted (limited by a minimum of 3 years of experience required)

### [CharityJob](https://www.charityjob.co.uk/?source=nav)

CharityJob is a job site that also includes voluntering opportunities. CharityJob allows a volunteer poster to use their free tier which only allows a poster to keep the advert up for 90 days. They also have other tiers which depending on the funding of the charity could allow things postings being featured to relevant candidates, appear at the top of search results and be included in email alerts. For more on the price plan see [here](https://www.charityjob.co.uk/recruiters#:~:text=Compare%20your%20options)

<h4>Pros: </h4>

- Easy and free to make a posting
- Great testimonials
- Works with a lot of charities already

<h4>Cons: </h4>

- Less likely to be seen due to the mix of job roles and volunteering roles
- Less features than other sites due to paid features

### [Do It](https://www.doit.life/)

With their home page giving more information on themselves than their [about me](https://www.doit.life/about) page, its hard to say exactly what do it does, but it seems to be in the same vein as [reach volunteering](#reach-volunteering). Looking at the stakeholders website, there are volunteering job postings that originally pointed to doit, which means the stakeholder is already accustomed to them. 

<h4>Pros: </h4>

- Unlimited advertisement posting
- Free posting
- High user count
- GDPR compliant

<h4>Cons: </h4>

- Get lost in advertiser noise
- Possibility to get flagged as spam or lost in a sea of fake postings

### A look into random charities from around the UK 

In this process, I am looking into how charities in more wealthy areas **and** poorer areas operate. This is to get more of a financial idea on how these charities operate too. With this I can surmise on the technologies and practices that lower income and higher income charities operate on average. For example a higher wealth area charity _might_ use [redis](https://redis.io/) to cache user queries and have multiple on site machines to host web servers. Whereas a less wealthy area may only have a basic [static website](https://en.wikipedia.org/wiki/Static_web_page) with a link to a google form that employees at the charity sift through themselves with no automation. I am not going to state the areas of which have higher or lower wealth on average. However, I am using the [2021 cenesus map](https://www.ons.gov.uk/census/maps/choropleth/population/household-deprivation/hh-deprivation/household-is-deprived-in-one-dimension) from the [Office of national statistics](https://www.ons.gov.uk/). The reason im looking into localised charities specifically is to better align technological methodologies that work to what the stakeholder requires. 

#### [TogetherCo - Brighton](https://togetherco.org.uk/)

<h4> How do they get volunteers? </h4>

- Volunteer section on website
    - Has specific role postings
    - Has a form to fill out to then have a [discussion with the charity](https://togetherco.org.uk/volunteer/#:~:text=We%20will%20contact,you%20might%20have.) on whats best for you in terms of volunteering

<h4> How is the process applying to be a volunteer and what systems are cleary visible</h4>

So this charity uses a [form](https://togetherco.org.uk/volunteer-application/) to get information from the user, likely to store in a database or straight to a CSV based file. After the user clicks submit and the information is valid, it will be sent off to a server so its hard to gauge what systems are in place.  

<h4> how do they facilitate companies/organisations to post volunteering opportunities </h4>

Doesn't have any clear indicator on how to facilitate this. Might go through a seperate company like [Reach](https://reachvolunteering.org.uk/)

#### [Manchester Community Central  Manchester](https://manchestercommunitycentral.org/volunteer-centre-manchester)

<h4> How do they get volunteers? </h4>

They have a section on their [website](https://manchestercommunitycentral.org/volunteer-centre-manchester/i-want-volunteer) which speaks about current opportunities. They also mention a in person drop in. While not necessary to book a slot, it is possible to do so via E-Mail or using the [calendly service](https://calendly.com/).

<h4> How is the process applying to be a volunteer and what systems are cleary visible</h4>

You can use the form at the bottom of [this page](https://manchestercommunitycentral.org/volunteer-centre-manchester/i-want-volunteer#:~:text=Volunteer%20Newsletter) to fill in a newsletter form. This indicates that either an employee CCs and email to a list of people or some automated newsletter platform. From a quick google, platforms for automated newsletters exist like:

- [CleverReach](https://www.cleverreach.com/en/newsletter-tool/creating-and-designing-newsletters/?tl=o8ejlo-aw_uk_cn&gad_source=1&gad_campaignid=1370877092&gbraid=0AAAAADj-Y5p11HESNGlfDIL4UX7zsALFv&gclid=CjwKCAjwxITRBhBYEiwA6mZm7ZlYPj1hoQf-Fzp6Ay-qqrejPVhJTuu8OYbZEhog0A4dmfQC6n6xlBoCZxUQAvD_BwE)
- [Exclaimer](https://exclaimer.com/lp/14-day-free-trial/?hstk_creative=810959687171&hstk_campaign=23892133625&hstk_network=googleAds&creative=810959687171&keyword=email%20brand%20consistency&matchtype=b&network=g&device=c&utm_term=email%20brand%20consistency&utm_campaign=UK%20%7C%20Search%20%7C%20Generic%20%7C%20Broad%20Match%20A%2FB%2FC%20Landing%20Page%20Test&utm_source=adwords-search&utm_medium=cpc&utm_content=Broad%20-%20Brand%20Identity&hsa_acc=4500841410&hsa_cam=23892133625&hsa_grp=195322110445&hsa_ad=810959687171&hsa_src=g&hsa_tgt=kwd-2424627345829&hsa_kw=email%20brand%20consistency&hsa_mt=b&hsa_net=adwords&hsa_ver=3&gad_source=1&gad_campaignid=23892133625&gbraid=0AAAAADzh7UANuNVAaIuF3fxvl9toXU9L-&gclid=CjwKCAjwxITRBhBYEiwA6mZm7UwT0Ct1B1Qu8LeeRH96L80FVK0YAwWXM3-chf2Cw3-fzRebgScf5hoCSUwQAvD_BwE)
- [Monday campaigns](https://monday.com/crm/lp/campaigns?cq_src=google_ads&cq_cmp=23044226584&cq_term=email%20marketing%20software&cq_plac=&cq_net=g&cq_plt=gp&utm_medium=cpc&utm_source=adwordssearch&utm_campaign=gb-en-prm-workos-monday_campaigns-email_marketing-h-search-desktop-core-aw&utm_keyword=email%20marketing%20software&utm_match_type=p&cluster=crm_industries&subcluster=crm_healthcare&ati=&utm_adgroup=email%20marketing&utm_banner=775017905004&gad_source=1&gad_campaignid=23044226584&gbraid=0AAAAADeiQJuzMvjpNP5Fb8wJ0IXbxiNiK&gclid=CjwKCAjwxITRBhBYEiwA6mZm7Z7wvFhfbakc2QlzwoKGuzz8tRepHgZ_hfrbt0brv2AbROvnt8Z1aRoCZQ0QAvD_BwE)

All of which cost money (with free trials available), but self hosted systems might work better for cost effectiveness. Like a simple server running [python code](https://www.python.org/) using the [gmail API](https://developers.google.com/workspace/gmail/api/quickstart/python). You could even use the website's volunteering posts to generate new newsletters every week by [webscraping](https://en.wikipedia.org/wiki/Web_scraping)

There is also [this page](https://manchestercommunitycentral.org/volunteer-centre-manchester/view-opportunities) which gives lists of job postings and allows searching for specific postings like when the volunteer work runs, where its located, area of interest and keyword searching. However this page is quite messy and hard to navigate

<h4> how do they facilitate companies/organisations to post volunteering opportunities </h4>

As an organisation, you can go through a step by step form process asking for specific questions and then it says you can expect to be contacted within 5/10 days. 

#### [wtonvolunteers  Wolverhampton](https://wtonvolunteers.org/)

<h4> How do they get volunteers? </h4>

You sign up for an account on their website and that gives you access to their [apply for opportunities page](https://wtonvolunteers.org/choosing-opportunities/apply-here/). Their registration requires approval, which would weed out spam accounts for the volunteer side of things. Might use a simple form on the front end and have a human manually go through the registrations. However I am unable to gather how the volunteer application process goes ahead at this time. 

<h4> How is the process applying to be a volunteer and what systems are cleary visible</h4>

This is obfuscated to me at this time because you require to be approved to gain access to their webpages that facilitate volunteer applications. This might just be as simple as a database storing user accounts, hashing the password and then comparing the login hash to authenticate user login and then using session cookies to keep them logged in. With the auth of the user, they can then access content from the charity. 

<h4> how do they facilitate companies/organisations to post volunteering opportunities </h4>

They provide a [doc for organisations to register](https://app.box.com/s/x18ra9o5fbduex30xs8mwy2ighabzobp) and also [a doc for volunteering opportunities to be registered too](https://app.box.com/s/5xf7jcmosjv1he6pndilvkyysutkv5ix). They use a service called [box](https://www.box.com/en-gb/home?url_redirect=direct) which is used to host documents. This seems like a cost heavy idea for something that could be done in a form like what is already seen on the wesbite


#### [The Kids Network London](https://www.thekidsnetwork.org.uk/i-want-to-mentor?gad_source=1&gad_campaignid=22790719866&gbraid=0AAAAADRkgo9ZgrjOC3w8BTZU-XkR_5Yrm&gclid=Cj0KCQjw_vnQBhCxARIsADcZyxJlH0f1fgNgS3j_ExdetIzvqbD3oBxhusiLByw8EieP9HI863fcQbQaAlPtEALw_wcB)

<h4> How do they get volunteers? </h4>

A simple form is used on their website and is most likely stored or generated into a CV like PDF for manual review. 

<h4> How is the process applying to be a volunteer and what systems are cleary visible</h4>

No extra information needed. 

<h4> how do they facilitate companies/organisations to post volunteering opportunities </h4>

Not entirely applicable to this but they use [calendly](https://calendly.com/) to book a call or they take an email for communications

#### [Volunteer Centre Newcastle Newcastle](https://volunteercentrenewcastle.org.uk/)

<h4> How do they get volunteers? </h4>

<h5> under 18's </h5>

A [page](https://volunteercentrenewcastle.org.uk/young-volunteers) with a carousel that shows top opportunities that under 18s can apply for

<h5> over 18's </h5>

Same as the under 18's section but with proper listings for 18+ postings. 

Both contain a postcode field and keyword field to search up postings that then does show a proper list of postings in proximity to the postcode. 

<h4> How is the process applying to be a volunteer and what systems are cleary visible</h4>

Once you have an account, you can register for postings. Registering is just a simple form which allows you to state availability and also lets you sign up for their newsletter.

<h4> how do they facilitate companies/organisations to post volunteering opportunities </h4>

They use [Office365](https://www.office.com/) to facilitate companies filling in forms. They have [a form](https://forms.office.com/pages/responsepage.aspx?id=Rl7moRJ77kqULnLUi60mf7OdWObtaC5LlHQTimcI7jNUM1BXQUVMRzlVWUhTQjY4VkEwSlRXMlc4VS4u&route=shorturl) for companies registering with the charity and [another](https://forms.office.com/pages/responsepage.aspx?id=Rl7moRJ77kqULnLUi60mf7OdWObtaC5LlHQTimcI7jNUMEdDVkRKTkRFMUExNVFTMjcxRkFYVjNDTi4u&route=shorturl) for companies to post their advertisements directly. Most likely somebody is manually going through all of the forms themselves. 

#### [Vast Stoke on Trent](https://vast.org.uk/)

<h4> How do they get volunteers? </h4>

Much like many websites thus far, you will be filling out a [form](https://vast.org.uk/upload-your-opportunity/) and submit it for a review. There is also a system to [search for opportunities](https://vast.org.uk/volunteer-opportunities/) too. What is concerning is the entire list of postings might be on the page to begin with which would concern the client with loading times possibly pushing a user with slower internet away. 

<h4> How is the process applying to be a volunteer and what systems are cleary visible</h4>

Submitting a volunteer posting is the same as applying to be a volunteer too. A [form](https://vast.org.uk/upload-your-opportunity/). They also provide some sort of [system](https://vast.org.uk/calendar/) to see events coming up sorted by soonest to latest

<h4> how do they facilitate companies/organisations to post volunteering opportunities </h4>

They have a [small form you can fill in](https://vast.org.uk/contact-us/) and it seems like this is their preference but they also provide a phone number, email address and a number for whatsapp communications

#### [BVSC Birmingham](https://www.bvsc.org/)

<h4> How do they get volunteers? </h4>

They have a [listings page](https://www.volunteerbrum.org/volunteer/all/activities?search_radius=50) of volunteer opportunities. However you are required to have an account to apply for such positions. 

<h4> How is the process applying to be a volunteer and what systems are cleary visible</h4>

Its not that good, they have a whole other [website](https://www.volunteerbrum.org/) which doesnt come up at the top of search results for "birmingham volunteer charity" or searches like it, which is misleading and makes it harder to look for volunteering opportunities for the average user. Information on the process is also included in this section's "How do they get volunteers?" section. 

<h4> how do they facilitate companies/organisations to post volunteering opportunities </h4>

You can become an [organisational member](https://www.bvsc.org/join-now#:~:text=of%20these%20options.-,Become%20an%20organisational%20Member%20of%20BVSC,-BVSC%20is%20proud) of BVSC. You can also [promote](https://www.bvsc.org/promote-your-organisation) through the BVSC. There is also a way to [work directly with BVSC](https://www.bvsc.org/work-with-us) which might provide a better outcome.  After further investigating, there is also [this page](https://www.volunteerbrum.org/for-organisations) which provides a way to make an account to be able to post opportunities with. 

#### [rainbows](https://www.rainbows.co.uk/)

<h4> How do they get volunteers? </h4>

They have a [listings page](https://rainbows.goassemble.com/opportunities/results#display=grid&s=date_advertised&o=desc&limit=14&include=image&public_search=true) to see all postings. 


<h4> How is the process applying to be a volunteer and what systems are cleary visible</h4>

Its a [multi step form](https://en.wikipedia.org/wiki/Wizard_(software)) for each posting where you put your details down that seems to double as an account set up (earlier in the form you put your email and address and at the end you write a password to use). A weird mechanism but im assuming having an account auto applies all this information automatically. 

<h4> how do they facilitate companies/organisations to post volunteering opportunities </h4>

Due to this charity being closely tied to childrens hospice, there isnt anything in terms of volunteer postings. However I can still look at this charity for terms of the prospective volunteer.


## Taking the ideas head on

### I want to prepare a database that can deliver a VOLUNTARY SECTOR JOB MATCH

A database might not be the most ideal idea for this straight away unless some app, API and/or website is needed. For a small company in the volunteering sector it might be better to utilise already existing technologies to minimise costs.

#### Usage for an app

A database for an app makes perfect sense. If you require an app, to store user accounts, volunteer postings etc, you will need a database to store this information

#### Usage for a API

This would be more of something like an [API](https://en.wikipedia.org/wiki/API) that developers could use to grab local volunteer listings from your repository and deploy it to their apps and/or websites. 

#### Usage for a website

Much like the app perspective, it makes perfect sense. The same usages you would have for a databse for an app, you would have for a website too. In fact, your website and app could be pulling from the same server but using their respective technologies (like a [web browser](https://en.wikipedia.org/wiki/Web_browser), [app framework](https://developer.android.com/studio?gclsrc=aw.ds&gad_source=1&gad_campaignid=21831783765&gbraid=0AAAAAC-IOZlBp3YbgXT-JrGgb1AAgF07y&gclid=Cj0KCQjw_vnQBhCxARIsADcZyxKEUWY1-eJuf-FFt4QEOMyA0PQYZ2OeX3fH-dCSjJoNFEm91e08zBYaAuExEALw_wcB))

#### Consensus on topic

<h3>Low cost</h3>

A low cost methodology for this would be based on using [google forms](https://docs.google.com/). The reasoning behind this is that it is **FREE** and can be easily converted to a .csv file for viewing in something like [Microsoft Excel](https://www.microsoft.com/en-gb/microsoft-365/excel) or [LibreOffice Calc](https://www.libreoffice.org/). However a user will have to manually click the generate csv button on the forms page and then open it and manually go through it. Granted, if they are used to the software, they could perform expressions to sift through data. On the charity website, a link to the form will be required. 

**Pros vs cons**

- Pros

    - Free
    - Can take all the required data
    - Reliable (because its using a big 3rd party platform)
    - No sign up is required to apply for a volunteering role and spam can relatively be filtered out because an email address is required to submit a form application
    - Form can be used to facilitate companies posting their volunteer roles

- Cons
    - Manual user review
    - Possible bot account problem (if they use [burner emails](https://en.wikipedia.org/wiki/Disposable_email_address) or [stolen emails](https://en.wikipedia.org/wiki/Email_hacking))
    - Does not work well for a small team of employees to sift through loads of information 
    - A lot of people could be missed out on volunteering opportunities due to user error
    - User error could mismatch people with the wrong opportunities
    - Employee working with data must know what roles match with what opportunities rather than having users match automatically
    - Employees must contact organisations for the match rather than the user being able to contact directly 

<h3> Medium cost </h3>

An automation platform would be a medium cost effective way to go about this when looking at the [n8n platform](https://n8n.io/). Why is this? Well we can have multiple forms, pages etc to take on user interaction and automate the entire process. We can have systems that are frequently checking users against volunteering opportunties to properly match them with roles and have Ai systems help users progress their careers via voluntary roles. 

**Pros vs cons**

- Pros

    - Automation
    - Provides a [front end](https://en.wikipedia.org/wiki/Front_end_and_back_end) for all needed services
    - AI powered 
    - Contains a lot of 3rd party services like [survey monkey](https://www.surveymonkey.com/) and [Gmail](https://www.google.com/gmail/about/signup_complete.html)
    - Has AI chat assistant that _**sometimes**_ helps out with problems encountered in the automation process

- Cons
    - Requires somewhat knowlegeable user to set up the initial systems

<h3> High cost </h3>

A high cost methodology would be something that can withstand high user bandwith and be error corrective and automatic. First we will need to store user accounts, this will be done to avoid spam applicants and [scrapers](https://en.wikipedia.org/wiki/Web_scraping)

**Pros vs cons**

- Pros

    - pro1

- Cons
    - con1

### I may mean VOLUNTARY SECTOR SKILLS match

#### Consensus on topic

<h3>Low cost</h3>



**Pros vs cons**

- Pros

    - pro1

- Cons
    - con1

<h3> Medium cost </h3>



**Pros vs cons**

- Pros

    - pro1

- Cons
    - con1

<h3> High cost </h3>



**Pros vs cons**

- Pros

    - pro1

- Cons
    - con1




### There is also an element of CAREER DEVELOPMENT in the **REDACTED** voluntary sector

#### Consensus on topic

<h3>Low cost</h3>



**Pros vs cons**

- Pros

    - pro1

- Cons
    - con1

<h3> Medium cost </h3>



**Pros vs cons**

- Pros

    - pro1

- Cons
    - con1

<h3> High cost </h3>



**Pros vs cons**

- Pros

    - pro1

- Cons
    - con1






### I don’t know what there is nationally of a similar offer.

#### Consensus on topic

<h3>Low cost</h3>



**Pros vs cons**

- Pros

    - pro1

- Cons
    - con1

<h3> Medium cost </h3>



**Pros vs cons**

- Pros

    - pro1

- Cons
    - con1

<h3> High cost </h3>



**Pros vs cons**

- Pros

    - pro1

- Cons
    - con1



### I wish to avoid GDPR issues with information we hold or share

#### Consensus on topic

<h3>Low cost</h3>



**Pros vs cons**

- Pros

    - pro1

- Cons
    - con1

<h3> Medium cost </h3>



**Pros vs cons**

- Pros

    - pro1

- Cons
    - con1

<h3> High cost </h3>



**Pros vs cons**

- Pros

    - pro1

- Cons
    - con1




### I need people to register to use the service , and have a charge for users to generate income for its management.

#### Consensus on topic

<h3>Low cost</h3>



**Pros vs cons**

- Pros

    - pro1

- Cons
    - con1

<h3> Medium cost </h3>



**Pros vs cons**

- Pros

    - pro1

- Cons
    - con1

<h3> High cost </h3>



**Pros vs cons**

- Pros

    - pro1

- Cons
    - con1






### It will need to describe knowledge areas, skills, previous or type of project/ work done and seeking as well as work areas considered .

#### Consensus on topic

<h3>Low cost</h3>



**Pros vs cons**

- Pros

    - pro1

- Cons
    - con1

<h3> Medium cost </h3>



**Pros vs cons**

- Pros

    - pro1

- Cons
    - con1

<h3> High cost </h3>



**Pros vs cons**

- Pros

    - pro1

- Cons
    - con1





### It could also have  a “ jobs available “ / skills Im looking for section

#### Consensus on topic

<h3>Low cost</h3>



**Pros vs cons**

- Pros

    - pro1

- Cons
    - con1

<h3> Medium cost </h3>



**Pros vs cons**

- Pros

    - pro1

- Cons
    - con1

<h3> High cost </h3>



**Pros vs cons**

- Pros

    - pro1

- Cons
    - con1





### Id like to have a reporting facility to check number of users  

#### Consensus on topic

<h3>Low cost</h3>



**Pros vs cons**

- Pros

    - pro1

- Cons
    - con1

<h3> Medium cost </h3>



**Pros vs cons**

- Pros

    - pro1

- Cons
    - con1

<h3> High cost </h3>



**Pros vs cons**

- Pros

    - pro1

- Cons
    - con1






## Collection of form questions used for a company/organisation to post volunteering postings
<h1> 
DO THIS AFTER LOOKING AT ALL CHARITIES </h1>

## Collection of form questions used to aquire a volunteer
<h1> 
DO THIS AFTER LOOKING AT ALL CHARITIES </h1>

