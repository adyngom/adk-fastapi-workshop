---
Title: "How to build and deploy with Vite JS"
Published: September 19, 2022
View Count: 52,453
Subscribers: 1,690
Description: "What Is Vite? Vite is the French word for fast and is a Javascript development server and bundler that delivers source files over ESM or ES6 modules making it blazing fast in things like start, reload and it also supports Hot Module Reloading or HMR. Vite is the brain child of Evan You the creator of the Vue JS framework but supports out of the gate building applications with React, Svelte, Preact, Vanilla JS and of course Vue. Typescript is also available for any of the mentioned libs. Let’s learn by doing. Let’s build and deploy a vanilla js Vite app and talk about some the features of this awesome next generation front end tooling ."
---

## Table of Contents
00:00 - What is Vite JS
00:43 - Build  and deploy a vite js app
01:00 - Npm or yarn init vite@latest
01:45 - Vite js scaffold libs options
02:07 - Switch into project and install deps
02:32 - Structure of a vite js Vanilla install
03:49 - Default scripts in package.json
04:30 - Run the dev server
04:48 - Quick CSS change
05:21 - Run first production build
07:36 - One way to check prod build locally
08:09 - Checking prod build in one step
09:37 - Build a small app vanilla js app
10:51 - Add a simple JS module
12:18 - Import module into main
14:41 - Let&apos;s add a second method to our module
18:01 - Helps focus on building your app
18:36 - Preflight steps before we deploy
20:14 - Use surge to deploy the project
21:08 - Check production URL in browser 
22:08 - And like that we are live 😉
22:50 - Subscribe and  visit coderscraft.dev

## Transcript

[0:00] [Music]

[0:06] hello and welcome today we're going to

[0:07] be talking about vid what is vit

[0:10] vid is the french word for fast vit is a

[0:13] javascript development server and

[0:15] bundler that delivers source files over

[0:17] esm or es6 modules making it blazing

[0:21] fast in things like start reload and it

[0:23] also supports hot module reloading or

[0:26] hmr

[0:27] vip is the brainchild of even you the

[0:30] creator of the vue.js framework but

[0:32] supports out of the gate building

[0:34] applications with react svalt preact

[0:36] vanilla.js and of course vue

[0:39] typescript is also available for any of

[0:41] the mentioned libs so let's learn by

Build and deploy a vite js app
[0:44] doing let's build and deploy a venula js

[0:46] vit app and talk about some of the

[0:48] features of this awesome next generation

[0:51] front-end tooling let's get to it

Npm or yarn init vite@latest
[1:00] so let's create a new vid app if you

[1:02] already have npm or yarn installed in

[1:04] your system you can just run npm

[1:08] init

[1:10] and here you will do vit

[1:12] at latest

[1:16] okay

[1:18] and it will ask you for

[1:20] um the vid project if you don't have it

[1:23] already installed it will ask you if you

[1:25] can install uh the vid project but i

[1:28] already have it in my system

[1:30] and i'm gonna give it a name let's just

[1:32] call it my

[1:34] vit

[1:36] project

[1:40] if i can type myvidproject

[1:43] okay and like i was saying earlier you

Vite js scaffold libs options
[1:46] can select any of this uh framework or

[1:49] lib libraries

[1:51] uh to get started i'm just gonna go with

[1:53] vanilla.js

[1:54] and i can choose between vanilla with

[1:57] typescript or just vanilla let's just go

[1:59] plain vanilla

[2:00] and you see it has scaffolded my project

[2:03] i can now

[2:04] follow the instruction that i see we're

Switch into project and install deps
[2:07] gonna cd into my vid project

[2:12] okay and i'm gonna run npm

[2:20] install all right pretty quick

[2:23] and before running npm run dev i'm just

[2:26] gonna open it into vs code so let's do

[2:30] code that

Structure of a vite js Vanilla install
[2:33] okay so i wanted to look at the

[2:36] structure first before going into

[2:38] running the project so you have

[2:41] a typical uh front-end structure with

[2:44] some node modules for all your

[2:46] dependencies

[2:47] you have a

[2:48] default index.html file and what is

[2:51] interesting it's not um isolated into

[2:54] like a public folder or something it's

[2:56] directly right here within the structure

[2:59] of your project

[3:01] and if we open this index.html

[3:06] we see that it has a main div app with

[3:10] id app

[3:12] it just targets uh this source main.js

[3:16] file

[3:17] but we don't see any css being

[3:20] loaded here from the get go

[3:24] opening the main.js file we see that the

[3:27] css is imported here directly so we can

[3:30] see that

[3:31] c es6 style imports

[3:34] are supported right out of the box okay

[3:37] and we will test that

[3:40] when we're going to make a few changes

[3:42] here but the very first thing now that

[3:44] we have um

[3:46] an idea of the structure which is pretty

[3:48] simple let's look at the package.json

Default scripts in package.json
[3:50] and the scripts that we have so we have

[3:53] these three scripts essentially that

[3:55] we're going to be using the dev script

[3:58] to start our local folder the build

[4:00] script which will like bundle our

[4:03] project for production and the serve one

[4:06] that is gonna

[4:08] allow us

[4:09] to look at like uh our production build

[4:12] but in our local environment so

[4:15] uh

[4:17] since we have already

[4:19] installed the project

[4:21] the dependencies

[4:24] let's open up the terminal here

Run the dev server
[4:30] and let's run npm

[4:32] run dev

[4:37] there you go that was pretty fast and

[4:39] then we can open the project at

[4:41] localhost 3000 and we have the default

[4:44] like uh vit

[4:47] install

Quick CSS change
[4:48] so let's go back to the css here

[4:52] and i'm just going to do

[4:54] a background

[4:56] color

[4:59] let's have a dark background color and

[5:02] for the font let's have a color

[5:07] of white

[5:08] okay so

[5:10] the hmr update is running and it has

[5:13] updated the style css and if we open our

[5:16] project we see that the styles have been

[5:18] applied

[5:19] perfect

Run first production build
[5:21] now

[5:22] let's um

[5:25] let's try to build the project so let me

[5:29] and by the way

[5:31] if you're gonna use serve

[5:33] um it is assuming that you already have

[5:36] build a project so the build the serve

[5:40] is going to be looking for your dist

[5:41] folder

[5:42] in order to serve you that application

[5:45] locally

[5:46] so

[5:47] if you really want to be able to use a

[5:50] serve

[5:51] i will maybe add

[5:54] the

[5:54] npm

[5:56] run build

[6:00] and

[6:02] viet preview so that it allows you that

[6:04] anytime you run serve you already have

[6:07] like the build that is done first if you

[6:10] miss that step

[6:11] it will not be able to target like the

[6:13] this folder is looking for so but let's

[6:16] assume that we just want to

[6:18] build first let's go back to the

[6:20] terminal

[6:22] and just go npm run build

[6:27] okay

[6:29] there you go now you have the this

[6:31] folder that has been created

[6:33] everything that you need as dependencies

[6:36] are going to be in assets

[6:38] and you see that in assets your

[6:41] index

[6:44] your index css and your index.js file

[6:48] are gonna have some hashes in there

[6:50] i think the hashes are there for caching

[6:52] and for fast reloading so correct me if

[6:55] i'm wrong anybody who knows more about

[6:57] it and then in the index.html file in

[7:00] the this folder

[7:02] one interesting element here there are

[7:05] many interesting elements but one that

[7:07] caught my eye is this cross origin

[7:09] attribute

[7:11] so this cross origin attribute

[7:14] uh since you're gonna be uh

[7:16] going into the local file system

[7:19] i think it is here in order for you to

[7:22] be able to get uh

[7:24] that without having a course issue

[7:27] okay

[7:28] so but view um not view vit is very well

[7:32] documented you can double check on that

[7:34] uh um and that assessment so now if i

One way to check prod build locally
[7:38] want to serve this locally

[7:40] uh if i don't use serve i could just

[7:42] like this into my

[7:45] cd into the disk folder

[7:47] and i have the live server

[7:50] uh extension

[7:52] um

[7:54] installed here and i'm just gonna lie

[7:56] server into it and you see now we are at

[8:00] uh

[8:01] 8080 which is the default port for like

[8:04] the production view

[8:05] and we have our same vit app that is

[8:08] working in here so now we could do that

Checking prod build in one step
[8:10] in one step

[8:12] since we have

[8:14] and you see a live server is ready for

[8:16] changes but we don't want to be touching

[8:19] here this is our production app

[8:21] so let's just um exit out of it and

[8:26] let's just go back one folder up

[8:29] okay

[8:32] and we are

[8:35] in the right spot here

[8:36] command k

[8:38] yeah so now we could do that in one shot

[8:43] i'm gonna get rid of the this folder

[8:48] okay let's move it

[8:49] we don't have it anymore and now i want

[8:52] to run this serve command that will not

[8:54] only build but then serve at the same

[8:56] time so let's just go npm

[8:59] run serve

[9:04] there you go you see now it has created

[9:06] our this folder like i was telling you

[9:08] earlier

[9:09] and now it's exposing the app at

[9:12] localhost 5000 so

[9:15] and there you go we still have like the

[9:17] same app so these are like some of the

[9:21] things that you could do just to make

[9:22] sure that you have your development

[9:25] and your production

[9:29] application streamlined this way

Build a small app vanilla js app
[9:37] so

[9:38] now let's try to build um something with

[9:42] what we have here

[9:44] we're going to build uh

[9:47] i would say i i don't want to say

[9:49] useless but like a good example of a

[9:52] vanilla js app but

[9:54] the one thing that made me so excited

[9:56] about uh

[9:57] this uh this tooling is like the native

[10:01] es imports so let me

[10:06] go ahead here

[10:08] and i'm gonna create um

[10:12] i'm gonna create uh let's get rid of the

[10:15] this folder i probably could add it to

[10:17] my script

[10:19] uh but uh let me just get rid of the

[10:23] this folder

[10:25] and um at the root i'm gonna create an

[10:29] utils

[10:30] folder

[10:32] and in the utils folder i'm gonna create

[10:35] a test

[10:38] that module

[10:40] that gs file

[10:42] okay

[10:42] so

[10:44] for the test

[10:45] i'm gonna

[10:46] let's see we're gonna have a um

Add a simple JS module
[10:51] what can we do in here let's do

[10:54] something as simple as uh we're gonna

[10:57] export a test module

[11:03] we're going to export a test module

[11:06] and the completion is done by tap nine

[11:08] i'm gonna do a whole uh

[11:11] tutorial on top nine for code completion

[11:14] and ui support

[11:16] so here

[11:19] i just want it to be a function that is

[11:22] going to take a message

[11:25] and

[11:26] that message basically we're just gonna

[11:29] alert it okay we're just gonna alert

[11:31] back that message

[11:36] okay

[11:40] all right inside the utils folder let's

[11:43] create an index.js file

[11:50] index.js file and we're going to export

[11:53] all

[11:54] from

[11:56] and you see how top nine is completing

[11:59] uh it's helping me here look a little

[12:01] smarter

[12:02] so export all from and we have test

[12:08] module

[12:09] okay test that module

[12:14] and that's it

[12:17] nice

Import module into main
[12:18] all right

[12:19] now let's go back to our main.js file

[12:22] and in here

[12:24] i'm gonna import

[12:29] um

[12:30] test

[12:32] okay i can even do import from

[12:38] utils

[12:40] yep i can import from utils

[12:45] and here i can import

[12:49] test module

[12:51] i really like

[12:54] uh using it this way i don't have to

[12:56] start like a node server somewhere or

[12:59] you know this is just to me this is just

[13:01] like awesome already

[13:04] because i'm gonna be doing with dealing

[13:05] with the browser i don't have to take

[13:07] browserify and everything else i just

[13:10] like code the way that i do when i when

[13:13] i'm doing rapidly um prototyping like a

[13:16] vanilla js application

[13:18] okay so

[13:20] we have that and um here

[13:25] i'm just gonna add a set timeout

[13:30] okay

[13:31] and let's give it a second so 1000

[13:36] okay

[13:38] and let's just call test module

[13:43] vit

[13:46] is blazing fast

[13:52] okay

[13:54] top nine is messing with me right now so

[13:57] let's just uh

[13:59] keep it at that okay

[14:01] command s

[14:04] let's um let's make sure now we run npm

[14:06] run dev

[14:11] all right

[14:12] and let's go back to our

[14:15] local host one

[14:17] second and then we have vit is blazing

[14:19] fast this is awesome so we pretty much

[14:23] have

[14:25] a module here or like um you know how we

[14:28] would start defining a javascript module

[14:32] we are able to import it into our

[14:34] main.js file and v just like does its

[14:38] magic in the back and uh something very

Let's add a second method to our module
[14:41] cool for us okay let's add let's add

[14:43] something to our test module here

[14:46] and

[14:48] um

[14:49] gonna be fetching um some post uh types

[14:53] from like the json server typical json

[14:56] server so let's do

[14:59] export

[15:01] constant

[15:05] and it's going to be called i'm going to

[15:06] call it iffy post you know it's going to

[15:09] be something that is going to execute

[15:11] right away

[15:13] well you tell me why don't why do you

[15:15] even need to put it in a in a module or

[15:17] whatever but that's just for the example

[15:19] for the sake of example so here

[15:23] i'm going to put an iffy

[15:29] okay

[15:30] and

[15:33] let's make it an async function here

[15:37] and inside

[15:41] since i'm gonna be using the

[15:43] the fetch api i'm gonna do let query

[15:48] which is gonna be equal to fetch

[15:53] okay

[15:55] and i don't think type code has https

[15:58] and that's going to be json

[16:02] placeholder

[16:05] type code

[16:08] dot com

[16:10] and i want to get all the post elements

[16:13] post

[16:14] plural so that's gonna be my query but

[16:17] i'm gonna wait for it

[16:20] okay next step here and uh we can give

[16:25] ourselves some space we don't need uh

[16:27] this side so let's just do command b

[16:30] here

[16:31] and let's go to the next one

[16:34] and this time we're gonna do let post

[16:37] yep oh i love that top nine already is

[16:40] giving me that await query

[16:43] this is cool man so query json

[16:47] all right

[16:49] and i'm just gonna log

[16:52] or console that log post

[16:55] so since this is an iffy basically we're

[16:58] gonna be able to see it uh

[17:01] uh

[17:02] execute right away

[17:04] uh do we need to import it into our main

[17:08] no i think since we have it all exported

[17:10] it's just gonna execute

[17:12] let me see if that's true so it says

[17:15] okay and

[17:17] okay so

[17:19] let's inspect here

[17:22] and let's go into our console and you

[17:24] see that our our

[17:26] our iffy uh immediately invoked

[17:30] function like expression i think that's

[17:32] what it stands for

[17:34] it has like executed and if we look at

[17:36] the network tab

[17:40] let's just refresh right here

[17:44] if it is blazing fast

[17:46] and if we look at the network tab

[17:51] we see that we have executed this post

[17:55] that went to typey code

[17:58] post so that's pretty cool and you see

[18:00] that i'm already

Helps focus on building your app
[18:02] even though

[18:03] i don't know if this is this can be

[18:05] called like uh a valid js application

[18:09] but you see the building blocks and what

[18:11] i really like about it i'm starting not

[18:14] to even worry about the tooling part i'm

[18:18] starting to focus on my functionality

[18:21] and what my app should look like

[18:23] and to me that is like priceless you

[18:26] know i really don't have to worry about

[18:28] that thing

[18:29] uh vit is taking care of it

[18:32] and that is just plain awesome so now

[18:35] the last step uh we're gonna get this

Preflight steps before we deploy
[18:37] ready for deploying it uh so we can

[18:40] share it with like you know um i don't

[18:43] know co-workers we can share it with

[18:45] like uh the client so let's do it and

[18:49] we're gonna be using

[18:51] there's a lot of

[18:52] options nowaday

[18:54] but

[18:55] i'm becoming a very big fan of surge

[18:58] search sh

[19:00] so

[19:01] so go to search and then get like um um

[19:05] an account in there

[19:07] and i'm gonna show you how fast you can

[19:09] deploy after you get an account the

[19:11] account is free and of course you can do

[19:13] more if you go with the

[19:15] with the paid version but out of the box

[19:18] what you get out of it is just it's just

[19:21] like super awesome so let's go back to

[19:23] our project here

[19:25] and first thing first

[19:29] i want to make sure that my production

[19:31] build is all right so i'm just going to

[19:33] do npm run

[19:36] server

[19:39] which creates like this folder so this

[19:42] is ready for production but at the same

[19:44] time i can look at it here

[19:47] locally

[19:49] okay vid is blazing fast okay and

[19:53] let me inspect

[19:55] and i see that

[19:57] the call has been made i have my hundred

[19:59] uh posts that are coming back from my

[20:02] api call

[20:03] perfect so let's say

[20:05] i have checked it and then everything

[20:07] works for my end-to-end testing or

[20:09] whatever you want to put in there before

[20:11] you push it to a production server

Use surge to deploy the project
[20:14] now i'm going to use search that i

[20:16] already have installed so if you don't

[20:18] have a search installed you will just

[20:20] use this npm install global search

[20:24] i already have it i'm not going to run

[20:26] it again

[20:27] so let's do

[20:29] command k here and i'm just going to do

[20:31] search

[20:33] so when i do search

[20:36] i'm gonna target here this folder

[20:40] and say this this is what i want you to

[20:41] push up okay

[20:44] so let's do that it's asking me

[20:47] if i'm okay with this domain i'm okay

[20:49] rpd plastic search why not

[20:53] and it's uploading it

[20:56] and then boom i have it now

[20:59] available

[21:01] at this url that i can copy

[21:05] come here

[21:06] command v

Check production URL in browser
[21:11] vit is blazing fast let's look at the

[21:13] console again

[21:17] okay so

[21:21] it's saying that it was loaded over

[21:24] https but requested an insecure resource

[21:27] content must be served over https

[21:31] okay let's see if we can do something

[21:33] about this

[21:34] um

[21:39] let me see if i just prefix it

[21:44] with http instead and that's just

[21:46] because we are requesting um

[21:50] there you go

[21:52] now we don't have a problem okay so just

[21:54] to be a little careful about that of

[21:56] course you can go into the config and

[21:59] then make sure um you you take care of

[22:03] um

[22:04] the

[22:05] the http tps issue

And like that we are live
[22:08] but this is just for a demo to show you

[22:11] real quick how to start with the vid

[22:13] project

[22:14] not have really to worry about like the

[22:17] bundling side of it not have to worry

[22:19] about

[22:20] you know the tooling side of it

[22:22] uh

[22:23] vit has like a very extensive like

[22:26] documentation so if you go to the get

[22:28] started you see all of these things that

[22:30] are there building for production

[22:32] deploying a static site so i highly

[22:35] recommend that you spend some time in

[22:37] there they have done a great job at

[22:39] documenting some of these steps but i

[22:42] hope this gives you a glimpse at like

[22:45] what is possible with this very cool

[22:47] next generation front-end tooling that's

[22:50] all i had for you today and please do

[22:52] not forget to subscribe and turn on your

[22:54] notification there is way more that we

[22:57] have for you in store i see you next

[23:00] time take care

