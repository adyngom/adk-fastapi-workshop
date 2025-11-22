---
Title: "Agent Development Kit (ADK) Masterclass: Build AI Agents & Automate Workflows (Beginner to Pro)"
Published: May 3, 2025
View Count: 258,414
Subscribers: 84,000
---
# Brandon Hancock ADK Masterclass Transcript

## ⏰ Video Timestamps: 
00:00 - Start
01:25 - Example Overview
04:20 - Example 1: Basic Agent
23:01 - Example 2: Tools
35:24 - Example 3: LiteLLM
43:49 - Example 4: Structured Output
53:13 - Example 5: Session, State, & Runner
01:14:13 - Example 6: Persistent Storage
01:30:58 - Example 7: Multi-Agent
01:52:05 - Example 8: Stateful Multi-Agent
02:13:40 - Example 9: Callbacks
02:38:15 - Example 10: Sequential Agents
02:48:13 - Example 11: Parallel Agents
02:58:58 - Example 12: Loop A
03:12:04 - Outro

# Video Transcript

[ 0:00 ] Hey guys, Google just released their new agent framework called Agent Development Kit and it is exploding in popularity.

[ 0:07 ] And in this ADK crash course, I'm going to take you from beginner to expert so that you can go off and build your own

[ 0:14 ] AI agents, automate your workflows, and add AI agents to your own applications.

[ 0:19 ] And if you're new to the channel, my name is Brennan Hancock and I've helped hundreds of thousands of developers

[ 0:24 ] learn how to build AI agents through my crash courses on Langchain and Crew AI. So, I'm super confident that I'll be

[ 0:31 ] able to help you guys as well when it comes to building AI agents with ADK. And to help you master ADK as quickly as

[ 0:38 ] possible, I've created 12 different examples that we're going to walk through in this crash course. And you're going to see that we're going to start

[ 0:44 ] off with the absolute basics of building an individual agent and gradually add in more advanced features until you're

[ 0:50 ] building multi- aent workflows with tool callings and much more. And because I want this crash course to be as beginner

[ 0:56 ] friendly as possible, we're going to walk through every example step by step so that we stay on the same page and so

[ 1:02 ] you can see just how easy it is to actually create AI agents with ADK. And to make things even easier for you, I'm

[ 1:08 ] giving away all the source code for all the examples you're going to see today completely for free. Just click that first link in the description below so

[ 1:14 ] you can download the 12 examples and kickstart your 80k journey. But enough talk. Let's go ahead and cover the 12

[ 1:20 ] different examples that we're going to be building together today and then dive into creating our first agent together. So here are the 12 different examples

Example Overview
[ 1:27 ] that we're going to be building together today inside of this crash course. And as promised, we're going to start off by

[ 1:32 ] building the absolute basics, and then we're going to gradually add in more complexity and features until you're

[ 1:37 ] building some really cool multi- aent workflows. Super excited to dive into this. So, let's go ahead and cover these

[ 1:43 ] one by one so you know exactly what we're going to be building throughout today. To start off, we're going to create our first agent, which is a

[ 1:49 ] single agent, so you can understand the core principles of creating agents inside of ADK. From there, I'm going to

[ 1:55 ] show you guys how you can add tools to provide different and more functionality to the agents you create and how you can

[ 2:02 ] access some of the pre-built tools that Google provides you. From there, I'm going to show you how you can bring in

[ 2:07 ] other models to ADK, such as bringing in OpenAI and anthropic models, so you're

[ 2:13 ] not just stuck using Gemini. Super excited that ADK allows for this functionality. Next, you're going to see

[ 2:18 ] how we can make sure our agents spit out structured outputs. This is super important to make sure our agents spit

[ 2:25 ] out, you know, specific JSON structures so that we can pass it over to other APIs and tools. Then you're going to see

[ 2:32 ] how we can update and make our agents have session and memory so that they can remember things between different

[ 2:38 ] conversations. After that, you're going to see how we can make our agents save data, specifically save their session

[ 2:45 ] and memory so that when we close out of the application and open it back up, these agents still have access to things

[ 2:51 ] we talked about earlier. So, this is where we're going to start adding in some database functionality. After that, things are going to start to get fun

[ 2:57 ] because we're going to start working on creating some multi- aent solutions where we're going to have our agents working together and we're going to

[ 3:03 ] start off with the basics and then you're going to after that start to learn how we can add in, you know, some

[ 3:08 ] session and memory to our multi- aent solutions so they can remember things as they're talking and working together.

[ 3:13 ] Finally, what we're going to do after that is add in the ability to add in callbacks. And simply put, when it comes

[ 3:19 ] to callbacks, agents have a certain life cycle of things that they do before they run, after they run, and while they're

[ 3:25 ] running. And call backs allow you to control every part of the agent life cycle. Really excited to showcase this

[ 3:31 ] functionality. And then finally, what we're going to work on is talking about different workflows that you can access

[ 3:38 ] inside of ADK. So, we're going to start off with working on sequential agents where we make sure agents always work in

[ 3:44 ] a specific order. agent one, two, then three. They always work left to right. Next, you're going to see how we can

[ 3:50 ] make our agents work in parallel to our agents. We're going to have three or four agents working on task in parallel.

[ 3:55 ] And then when they're done, they're all going to come together and combine their answer. And then finally, you're going to see how we can add in loops to our

[ 4:02 ] agents where our agents are going to continually work over and over and over until they achieve a desired output.

[ 4:08 ] Super excited. So, you guys are going to go from a complete beginner to an absolute pro after going through all

[ 4:13 ] these different examples. So, let's go ahead and dive into our first example of building your first agent with ADK. So,

[ 4:18 ] welcome to the first example inside the ADK crash course where we're going to focus on building and running your first

Example 1: Basic Agent
[ 4:25 ] single agent. And inside of this first example, we're going to walk through five steps together. First, I'm going to

[ 4:31 ] cover the core attributes of building your agent so you can understand how all the different properties work together

[ 4:37 ] in order to run your agent. Next, we're going to cover the folder structure of creating your agent. And this is super

[ 4:43 ] important because ADK requires a particular format in order for you to run your agents. Third, I'm going to

[ 4:49 ] walk you through the process of installing your proper dependencies in order to run all the agents that you're

[ 4:56 ] going to see in this crash course today. The fourth thing I'm going to show you how to do is access and download an API

[ 5:02 ] key just like this so you can run your agents. And then the fifth thing that we're going to cover today is running

[ 5:08 ] your agents. So, this is where we're going to kick things off so you can begin to chat with your agents and see just how effective they are at following

[ 5:13 ] instructions and just how easy it is to run inside ADK. So, without further ado, let's go ahead and cover our first agent

[ 5:19 ] together. So, when it comes to creating your first agent inside of ADK, let's walk through each of the core

[ 5:24 ] components. So, first things first, inside of ADK, you need to make sure you have at least one root agent. This is

[ 5:31 ] the entry point to all the requests that you're going to start sending over to all of your agents. So you need to make

[ 5:37 ] sure that you have a root agent. From there, when it comes to your agents, there's a few core properties that you're going to use over and over and

[ 5:43 ] over. The first one is going to be the name of the agent. As we run the agent later on, you're going to see this name

[ 5:50 ] pops up so we can say who's actually taking responsibility and generating the results for each of the requests we send

[ 5:56 ] in. It's super important that the name of this agent, greeting agent, matches

[ 6:01 ] the agent name over here. So you can see greeting agent inside of our folder structure. It must match this name right

[ 6:08 ] here. If they don't match, ADK is going to throw a fit and say, "Hey, I don't recognize this. I don't see it anywhere." So, let's make sure they

[ 6:14 ] match. The next thing that you're going to need to put in all of your agents is a model. Now, as I mentioned earlier,

[ 6:22 ] you can use any model from any framework. We'll talk more about this later on. So, you can bring in your Claude or OpenAI, but the easiest models

[ 6:28 ] to use are going to be your Gemini models. Now, for this tutorial, we're going to use Gemini 2.0 no flash for

[ 6:33 ] everything. But if you want to see all the other models that ADK or specifically Google has to offer, you

[ 6:40 ] can click this link right here and it'll take you over to their model dashboard right here. So you can see there are a

[ 6:45 ] few core models that they offer. Everything from Gemini 2.5 Pro, which is their smartest, most powerful model.

[ 6:52 ] They also have the 2.0 Flash, which is a toned down version of it. It's not as smart, but it's still really fast. Or

[ 6:57 ] they have their 2.0 no flash model which has access to all of the multimodal features such as images, audio,

[ 7:04 ] everything else. So, this is the one we're going to be using throughout the rest of this crash course. But what you

[ 7:10 ] could also see if you want to check out on pricing, you can come down one tab right here and review the pricing for

[ 7:16 ] each of the models. So, you can see in our case, we are using Gemini 2.0 no flash. And you can see when it comes to

[ 7:22 ] pricing for this model, it cost about 10 cent per million tokens, which is wild

[ 7:27 ] how cheap it is, for how smart this model is. And then when it comes to output prices, you can see it cost 40.

[ 7:33 ] So all around, this is a super super affordable model. And it's insanely capable as well. And it has a 1 million

[ 7:39 ] token context window, which is insane for how much information we can pass into this model. Okay, enough about the

[ 7:45 ] model though. Let's go go go back and cover the two other properties that you're going to see in every agent going

[ 7:50 ] forward. So, the next property is going to be the description. Now, the description will come more in play as we

[ 7:56 ] create our multi- aent solutions. But basically, when we're working with multi- aent solutions, the root agent is

[ 8:03 ] always looking to say, hm, I'm trying to work on this task. What other agents do I have access to that would do a better

[ 8:10 ] job at working on this task? So this description is a highle basically job

[ 8:15 ] overview of like hey I am this agent and here's what I specialize in doing and if

[ 8:21 ] you know if it was a copywriting agent so someone who specialized in writing the agent would go oh I'm working on a

[ 8:26 ] writing task right now cool I need to delegate to this other agent long story short it is to help agents figure out

[ 8:32 ] who they should delegate work to in a single agent though there's no delegation so we wouldn't need it okay now the final one and the most important

[ 8:39 ] one is going to be the instructions and the instructions are just like it sounds like. These are the instructions for

[ 8:44 ] telling the agent what it should do and how it should do it. So, you're going to see as we go out throughout the rest of

[ 8:49 ] this tutorial how we add in some really complicated instructions and Gemini 2.0 Flash is just going to handle it like an

[ 8:56 ] absolute charm. So, now that you've seen the core attributes of an agent, let's go ahead and start talking about the

[ 9:02 ] folder structure and why things are set up the way they are. So, here's everything you need to know about the folder structure of working with agents

[ 9:09 ] inside of ADK. So, first things first, inside of every project we work on, we're going to put our agents in folders

[ 9:17 ] just like this. And we are going to have a few core components in each one. We're

[ 9:22 ] going to have an init.py file and we're going to have av and we're going to have an agent. So, let's walk through what

[ 9:28 ] each one of these does at a high level. When it comes to our init.py file, this is basically telling Python, hey, I have

[ 9:35 ] some important information in here that you need to look out. In the case of our ADK agents, we're saying, "Hey, in this

[ 9:43 ] folder, that's what the dot means. I have an agent that you need to work on importing." So, this agent is basically

[ 9:49 ] pointing at this agent.py right here. Okay. So, that's the important thing. An ADK, it needs to know what agents it has

[ 9:55 ] access to. All right. The next one that you need to look at is thev file. Thev

[ 10:00 ] file is where you're going to store all your environment variables for your agents and all the other projects you

[ 10:06 ] work on. Now, what's important to note is you only need to have one EMV file and you need to keep it inside of your

[ 10:13 ] root agent. And in this case, we only have one agent. So, we only have to put it one place. Basically, it just goes in

[ 10:19 ] the root agent. However, later on, you'll see whenever we start to work on multi-agent solutions, we're going to

[ 10:24 ] have a bunch of agents and you don't need to put a&b in all of them. You just need to keep it in the root one. So, hopefully that makes sense. And then

[ 10:30 ] finally, the other thing is you need to have your agent.py file. And a quick

[ 10:35 ] reminder, you need to make sure that the name of this agent matches the folder.

[ 10:40 ] It has to be 1:1 or else it's going to throw some errors at you. And to make your life easier, speaking of a while

[ 10:46 ] back when I was showing thev file is I've created example for you. So when you're working on this on your own,

[ 10:52 ] you're just going to rename this toenv instead of example and then you're going

[ 10:58 ] to paste your API key here. Yeah. So that is the folder structure at a nutshell. Now, what I want to do is walk

[ 11:04 ] you through how you can install all the dependencies to actually run this agent. So, in order to do that, let me show you

[ 11:11 ] all the different commands you need to run. And I've got some source code and instructions to help make this even easier for you guys. So, when it comes

[ 11:17 ] to installing all the dependencies in order to run this crash course, I've tried to make it as easy as possible for

[ 11:22 ] you guys. So, first things first, there is a requirements.txt file. And basically all

[ 11:27 ] this does is it calls out the different packages that we want to install. The most important one is obviously Google

[ 11:33 ] ADK because this is what's going to give us access to the agent development framework. From there, I have a few

[ 11:39 ] other different libraries and dependencies that you guys are going to need. And you don't need them all now,

[ 11:45 ] but I've tried to set it up so that you guys only have to run the install command once and then you're good for the rest of the project. Okay. So, what

[ 11:52 ] we need to do is follow some instructions that I have set up for you guys to create an environment. Now, if

[ 11:58 ] you're very new to programming, basically when it comes to working with Python, every time you work on a

[ 12:03 ] project, you want to create an environment. That environment is going to install and contain all of the

[ 12:09 ] different libraries and dependencies you need. The reason why you want to do this is because each project has its own requirements, and you don't want to

[ 12:16 ] accidentally install all the requirements from project A, B, and C into one environment because it's going to just cause a ton of errors. So, we're

[ 12:22 ] going to create a single environment for this. install all the required dependencies and then we're good to run

[ 12:28 ] everything. So, here are the step-by-step instructions to create your virtual environment. And you can find these by looking inside of the root

[ 12:34 ] folder of the crash course. I have a read me right here for you guys. So, here are the commands we're going to run together one at a time. So, the first

[ 12:40 ] one is we are going to create a virtual environment inside the root directory of your project. though you can open up

[ 12:47 ] your terminal and type in the command right here. Python make a virtual environment and then put the virtual

[ 12:53 ] environment in thevnb folder. So I'm going to run this and I'm going to show you what it does. So it just ran and now

[ 12:59 ] you can see in the top left corner of your file explorer you can see we have a new folder. It's a blank virtual

[ 13:05 ] environment that has a few key components of what's necessary to run a Python environment. Now from there what

[ 13:11 ] we can do is we need to activate this new environment. So I'm on a Mac so I'm

[ 13:17 ] going to run this command but if you're on Windows you can run these commands right here. So let's go ahead and paste

[ 13:22 ] it in. And what this will do is it will now say hey you are now working with this virtual environment right here. And

[ 13:29 ] this is where what's going to allow you to install all of your dependencies. I actually just really quickly need to get

[ 13:35 ] out of another environment. Deactivate. You don't need to run that command. I just needed it. I was uh in a weird

[ 13:40 ] state. Okay, cool. So, now that we have everything set up, what you can do is install all of the dependencies. And

[ 13:47 ] what this will do is it will install all the dependencies and put them inside your virtual environment. So, you can see right now we barely have any

[ 13:54 ] packages in here. But when I run this command, what it's going to do is it's going to install everything that we

[ 13:59 ] called out right here, all of these. And you will see in just a second, this virtual environment is going to include

[ 14:05 ] a ton more packages. everything from Google ADK, some stuff to look up finance stocks that we're going to do

[ 14:10 ] later on, and yeah, tada. It now has a ton of additional packages. Okay, great.

[ 14:15 ] So, that is pretty much set up. And now what we can do is we are officially done with installing all of our different

[ 14:21 ] Python requirement packages in order to run this project. So, tada, everything is done. So, now we can move on to step

[ 14:28 ] four, which is where I'm going to show you how you can access an API key to run everything that we're going to be

[ 14:34 ] working on today. So, let me quickly walk you through how you can create your own API key. So, what we can do is

[ 14:40 ] follow the rest of the readme instructions and we're going to walk through these steps right here. So,

[ 14:45 ] first things first is we need to go over to Google Cloud and create an account.

[ 14:50 ] So, what you'll do is hop over to Google Cloud just like this and you'll need to sign up and create account if you

[ 14:57 ] haven't. Once you do create account, you'll click console. And this will take you to this page right here where you're

[ 15:03 ] basically in your root dashboard. And what we want to do is click in the top lefthand corner because we're trying to

[ 15:08 ] create a project. We want one project to run all these examples. So we'll click create new project. And I will call this

[ 15:16 ] we'll call it YouTube ADK crash course just like this. And what I can do from

[ 15:23 ] there crash course. And then what you can do from there is you might not have a billing account set up. You will need

[ 15:29 ] to create one and this is what will be charged to as you create your own

[ 15:34 ] request inside of this examples cuz if you remember Gemini Flash 2.0 costs like

[ 15:39 ] 10 cent per million tokens. So it's going to like you might get charged a penny by running all this project. But

[ 15:45 ] you need to create a billing account. Now if this is your first time creating a Google Cloud Platform account, you'll probably get a bunch of free credits. So

[ 15:51 ] you might not have to go through this process. But I still just want to show it to you. So once you're done, you're going to click create. And then tada,

[ 15:58 ] it's going to create all of your project and all the necessary underlying assets

[ 16:03 ] for it. And you can see once it's fully done, you can click select project. And what this will do is in the top lefthand

[ 16:09 ] corner, you can now see that you are working on the project you just created. Great. So let's head back over to our

[ 16:15 ] instructions because we just checked off one and two. And now we want to create an API key. So we're going to go to this

[ 16:21 ] link. So, I'm going to go ahead and paste it in and it will take us to a page just like this. Now, you might have to sign up for AI Studio. It's a little

[ 16:28 ] weird. I can't remember if you have to sign up for Google Cloud and both. So, you might have to do an extra sign up step. But the important thing is you can

[ 16:33 ] now click the create API key button. So, we're going to click this create API key. And we are going to type in the

[ 16:40 ] name of our project, which is YouTube ADK crash course. Once this is done, it's going to say create API key. And it

[ 16:47 ] should take just a few seconds to create that API key, but you need to copy it. So great, we're going to copy it. And

[ 16:53 ] please don't share this with anyone else. I'm going to delete mine right after the video, but click copy. And you

[ 16:58 ] are going to go over to your VNV file. So basics agent, greeting agent, and

[ 17:05 ] paste it right in here. So this is how you're going to set up your agent and and actually have it access your API

[ 17:12 ] keys that you just set up. Fantastic. So, we're now good. And you can refresh just to make sure it all worked.

[ 17:18 ] Fantastic. So, now if you look at mine, it's going to say YouTube ADK crash course. And mine was already hooked up

[ 17:24 ] to a billing plan cuz you just walked through that with me as well. So, you are good. Things are great. You can now start to use this API key to make

[ 17:31 ] request. So, now we're at the final step, which is going off and and running

[ 17:36 ] the actual agent itself. So, you can see it in action. So, let me show you how you can start to do that. And the first

[ 17:42 ] things first is we are going to clear out our terminal so that we can run our special commands to get everything

[ 17:47 ] working. So in order to run this agent, the first thing we need to do is change directory to make sure we are inside the

[ 17:54 ] basic agent folder. So you're going to cd and go into the basic agent folder. Great. So if we look in here, yep, we

[ 18:00 ] can see we have our greeting agent. Things are looking good. Now the special command that we are trying to run is

[ 18:05 ] called ADK. This is the CLI, command line interface tool for using agent

[ 18:11 ] development kit. So if you just type in ADK by itself, it's going to show you all the different options that you can

[ 18:17 ] run. So you can run these all of these right here. Now let's walk through them and then I'm going to show you the one we're going to use. So first things

[ 18:23 ] first, you could run the API server. And basically what this will do is it will

[ 18:28 ] create a endpoint so you can start to make API requests to your agent. So you'll be able to do like a quick

[ 18:35 ] request to like localhost slash API slash and then make a request to your

[ 18:41 ] agents. So that's what you could do there. The next one is you could run adkreate and this would create an agent

[ 18:47 ] folder for you. We have already have everything set up so you don't need to run create. Then it has a few extra

[ 18:52 ] commands you can run such as deploy which will deploy your agents to the cloud. I have a full tutorial on that.

[ 18:57 ] Definitely recommend checking that on my channel. Then you have eval which is basically like running test against your agent. a little outside the scope of

[ 19:04 ] this tutorial, but I'll have one coming up later. The next one is run, which will run the agents inside your

[ 19:11 ] terminal. So, you would be typing inside of your terminal right here to chat with your agents. And the best one that we're

[ 19:16 ] going to be using is ADK web. And this will spin up a really nice looking website for us to chat with our agents

[ 19:22 ] and give us access to seeing a lot of the underlying events and state and everything else that's going on inside

[ 19:28 ] of our agents. So, let me show you how you can run this. So, we're going to type in ADK web. And what this will do

[ 19:35 ] is spin everything up. And you can now see, all right, great. Your web server has started. You can go to this link to

[ 19:42 ] access the agents. So, we're going to hop over to our browser. Go over and you

[ 19:48 ] can now see that we have our web server up and running and we have access to our agents. So, let me give you a quick

[ 19:53 ] overview of what's happening and then we're going to start chatting with it. So up in the top lefthand corner, you have the ability to pick which agent you

[ 20:00 ] want to talk to. In our case, we only have a single agent. So it auto picks, oh, you're trying to chat with the

[ 20:06 ] greeting agent. Now, we're going to talk about a lot of these later on, but just know events are as we chat with our

[ 20:12 ] agent, you're going to be able to see like, oh, event one happened where we were trying to figure out who to work with and we made a response and you can

[ 20:18 ] see in real time all the events that happen. State, this is where we are going to store information with our

[ 20:25 ] agents. We're going to hop on to this in module five. Artifacts outside the scope of this tutorial. A session. A session

[ 20:31 ] is nothing more than a series of messages between us and the agent. So, you know, we can create multiple

[ 20:37 ] sessions to where we can have multiple different chats with the agent. And then the final one is vows, but we're not

[ 20:42 ] working on that in in here. Okay. So, let's go ahead and start testing out this agent. And as a quick reminder,

[ 20:49 ] this agent, we have told it to follow these instructions. you are a helpful assistant that greets the user. Ask the

[ 20:55 ] user's name and greet them by their name. So what we can do is say, hey, how are you? And then we can see the agent

[ 21:02 ] follows these instructions. To make things a little bit more personal, what's your name? My name is Brandon.

[ 21:08 ] And from there, the agent will go, hey, Brandon. It's greeting me by name. And you can see it actually working and

[ 21:14 ] following these instructions. Now, speaking of what I was talking about earlier is events. So every time I made

[ 21:20 ] a request, you could see these events in real time. And this is one of my favorite parts of ADK is their the ADK

[ 21:27 ] web feature because it allows you to explore what's happening with the agents in a super interactive fashion. So you

[ 21:33 ] can now see all right for our first event, we only had one agent up and running. And you can see the message

[ 21:40 ] that was passed into it. Sorry, you can see the response from the agent. And if you were to dig deeper into the event,

[ 21:46 ] you can see the request and the response. In the request, you can see

[ 21:51 ] the a few things. You can see the initial instructions. So this is were the initial instructions that we passed

[ 21:58 ] in. And it also adds the description of the agent as well. So basically, it's

[ 22:04 ] taking this information right here, the description and instruction, and putting it all into the system instructions.

[ 22:11 ] That's what it's doing under the hood. And then you can see the initial message we gave it. So, hey, how are you? That's what's popping up right here. And then

[ 22:17 ] finally, you can see in the response, it generates the response. So, yeah, that's everything that you need to know when it

[ 22:23 ] comes to creating and running your first agent. And just as a quick reminder, you guys are now a pro at understanding how

[ 22:32 ] to create an agent, the core properties. You're also a pro at understanding the folder structure of why we need to set

[ 22:38 ] up things the way we need to do. you know how to get your API keys and you know how to run your agents. So, what

[ 22:45 ] we're going to do next is hop over to the second example where you're going to start to see how we can add in some tool

[ 22:50 ] functionality and access some of the cool pre-built tools that Google gives us. Super excited so you could see this

[ 22:56 ] in action and start leveling up your agents. Let's go ahead and hop over to example number two. Hey guys, and welcome to example number two where

Example 2: Tools
[ 23:02 ] we're going to look at adding tools to your agents so that you can add in additional functionality and supercharge

[ 23:08 ] your agents. And in this example, we're going to walk through four different items. First, we're going to cover the

[ 23:14 ] different types of tools you can use with your agent because ADK is super flexible. Next, I'm going to show you

[ 23:20 ] how you can actually add these tools to your agents. Third, we're going to cover some of the best practices that you need

[ 23:26 ] to know about when building your custom tools. And then, we're going to also cover a few limitations that you need to

[ 23:31 ] know about when building tools. And then fourth, we're going to go off and run one of these agents with some tools so

[ 23:37 ] you can see everything in action. So let's go ahead and quickly cover the three different types of tools you can

[ 23:42 ] use inside ADK. So the three different types of tools you can use inside ADK are function calling tools, you can use

[ 23:48 ] some built-in tools provided by Google, and then you can use thirdparty tools. So let's walk through each one of these one at a time. So when it comes to

[ 23:55 ] function tools, this is what you're going to be using 99% of the time. This is where you create a Python function

[ 24:00 ] that you then pass over to your agent. So you can say, "Hey, like go find the weather, go look up stocks, whatever you

[ 24:07 ] want to do." This is what you're going to be doing most of the time where you create your own custom Python functions. Now, you could also use agents as tools.

[ 24:15 ] This one is a little bit more complicated and you'll see it in action later on when we work on multi-agent solutions, but there is a scenario when

[ 24:22 ] you'd want to wrap an agent as a tool. We'll talk about that later. Then there are longunning function tools. This is a

[ 24:28 ] little out of scope of this crash course cuz it gets a little bit more complicated, but just know it is possible. The next thing that you can do

[ 24:34 ] is use some of the pre-built tools Google provided such as Google search code execution and then rag. In this

[ 24:41 ] example, we're actually going to look at how you can use Google search inside of your tools, which is super powerful that

[ 24:46 ] you get it out of the box. A few important things to note before we dive in. Built-in tools only work with Gemini

[ 24:53 ] models. So, if you're using OpenAI or Claude, any of those, these built-in tools will not work. I had to find that

[ 24:59 ] out the hard way. And the third option is to use thirdparty tools. So if you've used the lang chain or crew AI, you can

[ 25:06 ] easily add in some of the tools in the libraries for these different frameworks and bring them over to ADK. A little

[ 25:13 ] outside the scope of this, but just know it is possible. And basically ADK is trying to make it as open as possible to

[ 25:20 ] all the models and tools that you could ever want so you can easily build agents and get them up and running. So, now that you've seen the different types of

[ 25:25 ] tools we can use, let's hop over to the code so you can see how you can start to add tools to your agents. So, let's go

[ 25:31 ] ahead and hop back over to the code. Okay, so here is a super simple example of an agent using the Google search

[ 25:37 ] tool. Now, I do want to call out a few things just because we are still working our way up on becoming an ADK pro. So,

[ 25:44 ] per usual, we are inside of a agent folder. This one's called tool agent.

[ 25:49 ] So, that's why we call this tool agent. They must match. Like we said earlier, we've picked the model and we've given a

[ 25:55 ] description just like we normally do. And the main change that you're going to notice now is we've created a new

[ 26:00 ] property and added it called tools. This is going to be a list of all the

[ 26:06 ] different tools you want to use with your agent. And in this case, we are going to use the pre-built tool from

[ 26:12 ] Google search. And as mentioned just a second ago, there are some additional built-in tools that you could use. So

[ 26:19 ] there is the Vertex AI search. So if you're going to be doing any rag queries, you can do this as well. And

[ 26:24 ] there's also the built-in code execution tool. Now it is important to note that when using agents just like this, you

[ 26:32 ] can only pass in one built-in tool at a time. So you could not do the Vertex AI

[ 26:38 ] search capabilities plus the code execution capabilities. You can only use one built-in tool at a time. So that's

[ 26:44 ] super important to note as you're creating these agents and working with built-in tools. So, now that you've seen a built-in tool, I want to go ahead and

[ 26:51 ] show you how you can also add in some additional tools as well. So, one of the

[ 26:56 ] other types, the first type that we talked about was adding in your own Python code as functions. So, let me

[ 27:02 ] show you what that looks like. So, what you could do is create a function called get current time. And let me walk

[ 27:08 ] through a few of the important things so we can get this up and running. So, we can do let me get all the imports

[ 27:14 ] working so you guys can see it in action. Fantastic. So here is another example of a tool and this is why I like

[ 27:21 ] this one so much. So you can see in order to create your own custom Python

[ 27:26 ] tool, all you need to do is make a function. You need to specify a few other things. You need to specify the

[ 27:34 ] return type. You need to specify a dock string. A dock string, just in case you're not familiar with it, this is how

[ 27:40 ] the agent determines what the function does and if it should call it. So if we give it a command saying, hey, please

[ 27:47 ] fetch the current time. Well, the agent will look through all the available tools that we have down here and it will

[ 27:55 ] see like, oh, I can see right now that I have access to the get current time tool. So I know because I have access to

[ 28:01 ] this tool and I know what this tool does. Yes, this is the tool I need to use to solve this problem. Now, there

[ 28:07 ] are a few other things when it comes to best practices that you need to know when creating tools. First things first,

[ 28:14 ] whenever you are returning the results of a tool, the agent framework wants you

[ 28:20 ] to be as specific and as instructional as possible. And sorry if that's not a

[ 28:26 ] word, but what I mean by that is it's super common for a lot of the time when people want to return stuff is they'll

[ 28:31 ] just go, "Oh, okay. I'm just going to return the results." Well, you don't want to do this because when the result

[ 28:39 ] gets passed back to the agent, it's not going to know like, well, what is this? Like, did you give me the current time? What what is this? So, when you are

[ 28:46 ] returning results back to your agent so that it can read the results and use the results in the answer it generates, you

[ 28:53 ] want to make sure the dictionary you create is as robust as possible. And if for whatever reason you do return

[ 29:00 ] something, just say like this for example, let's just say you return hello. What ADK is going to do under the

[ 29:06 ] hood is it is going to wrap the return statement into a to something like this

[ 29:12 ] where it's going to do result and then it's going to do hello. So ADK is going to do its best to wrap the results and

[ 29:18 ] it's always going to convert it to a dictionary just like this. So we want to be as helpful as possible and instead of

[ 29:25 ] ADK having to do the work and just saying generic result, we want to say no, this is actually the current time.

[ 29:31 ] This is the key and this is going to be the value. Now a few other things that didn't show in this example is sometimes

[ 29:37 ] you want to pass in variables. So whenever you want to pass in variables what you can do is just say I want to do

[ 29:45 ] format and then what you can do is pass in the type of it. So in this case we

[ 29:51 ] want to do a string. Now what you can notice is my current time function now

[ 29:57 ] includes a default value. This is what a default value looks like. It's when you have a property or a parameter and then

[ 30:04 ] you pass in some values after it. Default properties do not work inside ADK at the time of this recording. So

[ 30:11 ] never add in default values. They won't work and things will break. So instead, what you want to do is just pass in your

[ 30:18 ] properties with the types just like this and use them however you want. Okay, cool. So you've now seen how to create a

[ 30:24 ] tool and you've seen how easy it is to add tools to your agents. The only other

[ 30:30 ] thing I want to mention when it comes to some limitations is ADK when it comes to

[ 30:35 ] built-in tools is super particular. Meaning, if you wanted this tool to search to use Google search, great. That

[ 30:42 ] could work. If you wanted to work with current time and add in a few extra custom functions, great, you can do

[ 30:49 ] that. But what you can't do is add in built-in tools with custom tools. ADK

[ 30:55 ] breaks whenever you do that. So, I just wanted to call out this before we actually used it so that you could

[ 31:01 ] understand some of the limitations cuz when I was playing around with ADK for the first time and this was breaking on me, I could not understand why it was

[ 31:07 ] breaking. So, hopefully that saved you some heartache. So, now that we've covered some of the best practices on

[ 31:12 ] creating tools and you've seen how to add tools to your agents, let's go off

[ 31:18 ] and run these different agents with the different tools so you can see them in action. And to start off, we're going to

[ 31:24 ] start with Google search and then we're going to test it again using the current time so you can see it you can see it working. So let's get this up and

[ 31:30 ] running so we can work with Google search. We're going to head over to our terminal and start running it. So the first thing we need to do is open up our

[ 31:36 ] terminal. And what we want to do is make sure two things are happening. One, you want to make sure you've activated your

[ 31:42 ] virtual environment. Head back to the beginning of the video to check out instructions for to do that. And the

[ 31:47 ] second thing is you want to make sure you change directory to the tool agent folder. So this one right here. Once you

[ 31:52 ] have that set up, you can run ad web and this will once again spin up a website

[ 31:58 ] that allows you to interact with your agents. Now you can see that we have an updated agent here which is the tool

[ 32:04 ] agent. So I can say hey do you have any news about Tesla this week? And what

[ 32:11 ] this will do is go off search the internet using the Google search tool. So you'll see in just a second you can

[ 32:18 ] see yeah right here. So you can see the tool we called. So it's the Google search and it looked up specifically

[ 32:24 ] this query Tesla news this week. And from there it generated a basically a

[ 32:30 ] nice result that we can ask questions about. So you can see like oh the stock did this. Here's what happened for the

[ 32:35 ] Q1 results. Basically everything that happened this week in Tesla. And what's so cool is you can dive into all the

[ 32:42 ] different events that happened to see what was going on under the hood. So per usual, click on the event and you can

[ 32:48 ] see the tool agent now has new functionality. So the tool agent now has access to the Google search tool. And

[ 32:55 ] when you look inside of it, you can see per usual, you can see the instructions we gave it. And you can see the query we

[ 33:02 ] passed in. And when you look at the response, you can see when we scroll down just a little bit, you can see, oh,

[ 33:09 ] it went off and searched all these different websites for us. scraped all the information from a Google search and

[ 33:14 ] then gave it back to us. So, this is when we're starting to see the power of using tools inside of our agents. So,

[ 33:20 ] this one worked pretty well. What we're going to do now, I'm going to close out of this and we are going to change up

[ 33:25 ] the agent to start using the get current time tool. So, you can see this one in action. So, we're going to do get

[ 33:30 ] current time. We are going to keep this one just how it is. And now what we're going to do, close the kill the server.

[ 33:37 ] Try it again. ADK web. This will recreate the server once again. So we can check out our website. We'll open it

[ 33:44 ] up. So we still have a tool agent. And now we can say, hey, what is the current

[ 33:50 ] time? And when we run this one, we'll see a different type of function calling. So the last one was a built-in

[ 33:56 ] tool call. And now what we're doing is we're triggering our custom tools. So you can see we sent an event to get

[ 34:02 ] current time and then we got back a result from get current time. And the final answer was formatted and sent back

[ 34:08 ] to us. So all around super super nice, super helpful. And per usual, we can check out the events to see exactly what

[ 34:14 ] went down. So we can see in the first event, our tool agent now has new tools,

[ 34:20 ] in this case, get current time. And we can look at the request. We can see our updated request. We can see the message

[ 34:26 ] we sent over. And then we can check out the response. And this time you can say, hey, I'd like to do a function call to

[ 34:32 ] what function? Oh, the get current time function, the one that we just passed in. And we can step our way through the

[ 34:38 ] different events to see what's going on. So in the second event, you can see we're waiting for tool calls to happen.

[ 34:44 ] So this is basically yeah, it's making a call. And then the third event, you can see, okay, I got the result from current

[ 34:50 ] time. And you can see here what is the final result. So yeah, that is tool calling in a nutshell. And don't worry,

[ 34:56 ] we're going to be adding in a lot more tools throughout the rest of this examples inside this crash course. But

[ 35:02 ] to start off, I just want you guys to see the basics so you can see how everything works together, how to use built-in tools, custom tools, everything

[ 35:08 ] else. So, you now have leveled up as an ADK developer. And now we're going to move over to example number three, where

[ 35:15 ] you're going to learn how you can bring in OpenAI models and models from Claude inside of ADK. So, let's hop over to

[ 35:21 ] example number three. Welcome to example number three, where you're going to learn how to connect your ADK agents to

Example 3: LiteLLM
[ 35:27 ] other models like OpenAI and Claude. And in this example, we're going to first

[ 35:33 ] walk through a few of the core technologies you need to support this functionality. So, we're going to head

[ 35:38 ] over to light LLM and open router to understand what they are and how we need to use them. From there, we're going to

[ 35:43 ] dive into the code so you can see how you can configure everything up. And then finally, we're going to run the

[ 35:49 ] agents using these new models so you can see how everything works together. So, let's go ahead and head over to looking

[ 35:54 ] at Open Router and Light LLM. All right. So, the first technology we're going to be using to connect our ADK agents to

[ 36:00 ] all sorts of different models is Light LLM. And in case you haven't heard of Light LM before, it is a free library

[ 36:07 ] that you can use that handles all the complexities of working with different models like OpenAI, Claude, Llama. It

[ 36:14 ] handles all the complexities with each one of them and gives us one nice library to interface with all of these

[ 36:20 ] different models. So, here's just a quick example of what it looks like to work with Light LLM. So as you can see

[ 36:27 ] like I said it is a package but under the hood all it's doing is you pass in a

[ 36:32 ] model. So OpenAI claude whatever model you want to use you pass it in right here and then you just pass in a

[ 36:38 ] message. That's basically how light LLM works and under the hood it is handling all the different connections and all

[ 36:44 ] the different types and functions to make your life as easy as possible. So that's the first technology we're going to be using cuz ADK actually imports

[ 36:52 ] light LLM. you're going to see in just a second and it makes it even easier than what you see right here. The next technology we're going to use is Open

[ 36:58 ] Router. Now, Open Router is a tool that allows us to purchase tokens that can be

[ 37:05 ] used for any model. So, it is basically one tool that allows you to connect to

[ 37:10 ] OpenAI Claude and these are actually to make requests over to the different servers. So, you can look up any model

[ 37:16 ] that you want. So, we can look up OpenAI 04 Mini and you can see, yep, I have access to this model. Here's some

[ 37:23 ] information about this model. It is currently working. And here's how fast we're getting for tokens per second

[ 37:29 ] right now. And it carries some cost. Now, Open Router is not a free tool. It does cost money to use. And what you can

[ 37:37 ] notice whenever you sign up for an Open Router account because you need to do it. So, you'll just head over to Open Router, sign in, and what you'll do is

[ 37:44 ] you will buy credits. And whenever you buy credits, there's like a 3% or 5%

[ 37:49 ] increase on the cost to use credits. And outside of that, you can just use these tokens and credits to make requests to

[ 37:56 ] Gemini, OpenAI, Claude, whatever you want to do. So, make sure you go ahead and add in some credits here. So, just

[ 38:03 ] add credits. Once you're done, what you'll do is you will create an API key. This API key is going to allow you to

[ 38:10 ] have one key that you can use to access every model which is the beauty of using open router. So what we can do is click

[ 38:17 ] create key and we will call this ADK crash course and we'll click create. And

[ 38:23 ] now we will get an API key. So copy this API key and you will want to head back

[ 38:28 ] to your code and we are in project number three. So you'll want to go down to yourv and you will paste in this open

[ 38:36 ] router key. And that's all you need to do in order to get things up and running. So now that we've covered the

[ 38:41 ] core technologies and we have you a open router key, let's go in and actually look at the agent so you can see what we

[ 38:48 ] need to do in order to start communicating with these different models. So let's hop over to the agent. All right, so we just opened up our

[ 38:54 ] agent.py that's using light lm. So I want to cover a few of the core changes that we're making in order to start

[ 39:01 ] working with other models. So first things first, we need to make a import

[ 39:06 ] to use light LLM. And we can see we're importing this from Google ADK. And then

[ 39:12 ] specifically when it comes to the model we want to use, we are using light LLM because light LLM is one interface that

[ 39:18 ] allows us to communicate with all the different model providers out there. Now, when it comes to using light LLM,

[ 39:24 ] there's pretty much for most technologies and models out there, you only need to provide two pieces of

[ 39:30 ] information. The model and the API key. So, let's look at the model first. When

[ 39:35 ] working with light LLM, what you need to do is first define the provider. So, since we are using open router, we need

[ 39:42 ] to define the provider first. So, open router check. The next piece of information we need to define is the

[ 39:49 ] model family. So in our case, we're wanting to check out OpenAI. So we want to put OpenAI here. If we were wanting

[ 39:55 ] to use Claude, we would put Anthropic here. And then once you're finally done, you want to put in the specific model

[ 40:02 ] that you're using. So in this case, what we're saying is, hey, I would like to use the new model from GPT 4.1. And

[ 40:08 ] we're wrapping it all inside of this class. And what's so nice is all we have to do is pass this model we create into

[ 40:16 ] our agent. And that's all we need to do to get it to work. Now the other piece of information that you'll notice in here is we are saying hey I would like

[ 40:23 ] to look at my operating system and I would like to get a specific environment variable. In this case I would like to

[ 40:29 ] get the open router API key. So if you look in thev file that we created just a second ago that's exactly what we're

[ 40:36 ] doing. We're just pulling out this API key to use in our agent. Great. So let's look at what we're trying to do with

[ 40:43 ] this new model so we can run it and see in action. So in our case, we are creating a dad joke agent. So dad joke,

[ 40:49 ] dad joke. And we're saying, hey, you are a helpful assistant that tells dad jokes. Please only use the tool get dad

[ 40:57 ] jokes to tell a joke. So here's the custom function that we've created. It's a list of jokes. Just basically like

[ 41:04 ] knock-knock jokes. And we're saying, hey, please randomly pick a joke from

[ 41:09 ] this list. That's all it's doing. So what we can do is start running this agent so you can see it in action. So

[ 41:15 ] per usual, we are going to open up our terminal. We need to change directory to

[ 41:20 ] the proper project. So we're in example number three and then we can run adk web. ADK web will spin up our terminal

[ 41:28 ] or basically our web interface so that we can check out our new agent in action. So you can see great we have dad

[ 41:34 ] joke agent and we can say hey please tell me a joke and this will go off and

[ 41:41 ] do exactly what we did in the previous tool calls where we went off and made a a request to get the dad joke. We got

[ 41:47 ] the dad joke back and then finally it returned the dad joke from our tool call. So all around this is awesome. And

[ 41:52 ] the crazy part is we're not using Gemini for this. We're using Open AI. And as a

[ 41:57 ] quick extra note because I want to be as helpful as possible for you guys. If you want to see all the different compatible

[ 42:04 ] models for open router, I have a link that you can see in the source code. So, let me show this for you real fast. But

[ 42:10 ] this link right here will take you to light LLM docs. So, you can see how to connect to Open Router. And here's a

[ 42:17 ] list of some of the most popular models you can chat with. So, you can see everything from OpenAI. You can see we

[ 42:23 ] have our cloud models down here. But if you want to check out the full list of compatible Open Router models, you can

[ 42:30 ] click here in the docs and it'll take you over to Open Router. We looked at this earlier, but you can type in any

[ 42:36 ] model you want. So, if you wanted to use something from llama, you can type in, let's just say we wanted to do llama 4.

[ 42:44 ] So, what we can do here is you can see, okay, cool. I'd like to use this one. So

[ 42:49 ] if we wanted to use this model, what we would type in is we would go okay, I would like to use open router open

[ 42:58 ] router for slash and then I would type in meta llama/ the name of the model. So

[ 43:03 ] just know before you use any of these models right here, you always need to add open router before it to properly

[ 43:09 ] use it in your agents. Yeah, you have access to all models that are available. And if you just want to experiment, you

[ 43:16 ] can click on the rankings in Open Router and see what models are absolutely crushing it. So you can try them out for

[ 43:22 ] your own. So yeah, all around Light LLM plus open router is a huge cheat code when trying to interface with all sorts

[ 43:28 ] of models to really expand the capabilities of working inside of agent development kit. So yeah, that's a wrap

[ 43:34 ] for example number three. And now we're going to move over to our next examples which is focused on structure outputs to

[ 43:41 ] make sure our agents generate the proper type of data we wanted to spit out. So let's go ahead and hop over to example

[ 43:46 ] number four. Hey guys and welcome to example number four where we are going to look at the different ways we can

Example 4: Structured Output
[ 43:52 ] make sure our agents generate the proper structured data. And this is going to be super important as you build larger and

[ 44:00 ] larger agent workflows because you want to make sure agent A is producing the correct information in the right format

[ 44:05 ] for agent B or so you can take the information from agent A and pass it over to an API, another tool or whatever

[ 44:11 ] you want to do. So structured outputs are super important. So what we're going to do is first look at the docs to see what options we have available to us.

[ 44:18 ] And then second, we're going to look at a pre-built agent I've created for you guys so you can see the structured

[ 44:23 ] outputs in action and see what we have to do to get it up and running. And then finally, we're going to run the code so

[ 44:29 ] you can see everything in action. So let's go ahead and check out the docs. Okay, guys. So let's dive into the structuring data docs when it comes to

[ 44:36 ] ADK. Now, we're going to walk through the three different options real fast and I'll give you my feedback on all of

[ 44:42 ] them and just to give you guys a brief overview before we dive into the code and see these guys in action. So the

[ 44:47 ] first option you have is to define input schema. I personally dislike this one because it's very easy to fail. For

[ 44:54 ] example, if a the previous agent is saying, "Hey, I need to give you this

[ 45:00 ] information." And we say, "Cool. I'm expecting this other type of information." Things are going to break. So this one's a little bit too rigid. So

[ 45:06 ] I usually try to stay away from this one. But there is another format that you're going to be using all the time,

[ 45:12 ] which is going to be output schema. And basically what output schema does is it says okay AI agent I would like you to

[ 45:20 ] create and generate an output that looks like a specific class. So for example

[ 45:25 ] they have a great demo down here where you can say okay agent I would like you

[ 45:31 ] to please generate a output in the form of a capital output. So this is a class

[ 45:37 ] we define and you can see up here when it comes to the model it is a base model

[ 45:42 ] imported from pedantic. That's exactly what the doc said. And what you can see inside of it is we go, "Oh, okay. I want

[ 45:48 ] this agent to return a JSON object that has a single property in inside of it, a

[ 45:54 ] capital. This capital will have a string." And I know that basically some

[ 45:59 ] additional information to help the agent figure out what it should put here is a description of it. So I can see oh okay

[ 46:05 ] the agent is going to whenever we ask it a question return a object that has a capital and the capital always needs to

[ 46:13 ] be the capital of a country. So that's basically output schema in a nutshell.

[ 46:18 ] There is one quick constraint. So this is something you need to know before using this in the wild. It is you cannot

[ 46:24 ] use output schema when using tools or transferring information to other agents. So later on, don't worry. What

[ 46:31 ] we'll do is we'll have agent one, we'll just have agent one do all the complex thinking, pass the raw results over to

[ 46:37 ] agent two, and then agent 2 will be the one responsible for making sure the output schema is met. Okay. Now, here's

[ 46:43 ] the final thing. When it comes to output key, this is a special name we can give

[ 46:49 ] to say, hey, I would like to store all the information you generate from here to a specific spot in state. Now, we

[ 46:56 ] haven't talked about state yet. We will more in the next section, but just think of state as memory that all of your

[ 47:01 ] agents can access. So what you can say is, okay, great. This agent is going to

[ 47:06 ] find the capital. It's going to make sure the output looks like this. It's going to be an object that stores a

[ 47:12 ] capital name. And what it's going to do is it's going to save the capital to

[ 47:17 ] state. So what we could do is eventually look up state.found capital. And when we

[ 47:23 ] look up the found capital, we will be able to see the result that was generated here. And our other agents will be able to access this information.

[ 47:30 ] And this is one of the best ways to help, you know, agent one generate information and agent two look up what

[ 47:36 ] the previous agent did use that information for the next. So this is how we get to basically start having one

[ 47:42 ] shared area with all of our information and all of our agents can access it. And it's very structured so we make sure

[ 47:48 ] that our agents always have access to the information they need. So that was a ton. So let's actually look at a real

[ 47:53 ] world example so you can see this in action. So let's hop over to the code. Okay, so now we're in the code when it comes to working with structured

[ 47:59 ] outputs. And I promise a lot of those initial concepts we talked about are going to come together and make sense. So as you saw earlier, there was a few

[ 48:06 ] important things that we needed to add to our agent to get structured outputs

[ 48:11 ] working. The two most important ones were output schema. So this is what's going to define yes you need to return a

[ 48:19 ] object of this class type and you can see for this agent we defined our email content up here. So just a quick bit of

[ 48:26 ] background in this example we're trying to say hey agent it is your job to take in some text I give you and convert it

[ 48:32 ] into an email that has two options or two properties. It has to have a subject line and it has to have a body. So every

[ 48:39 ] time we give the agent information it will always return this type of structured data. Now, so a few other

[ 48:46 ] things that are important to note before we dive too deep into the instructions. You must for best results when working

[ 48:52 ] with agents. Whenever you're using an output schema like this, you need to do

[ 48:58 ] a good job of defining what the schema is beforehand. So, for example, in the

[ 49:03 ] instructions, you need to do a good job of saying, "Yep, I would like you to return JSON matching this structure

[ 49:10 ] subject and body." That's exactly what we defined up here, but we need to put it in our instructions as well. The

[ 49:16 ] reason why we need to do this is if we don't tell the agent what type of data it needs to return whenever the agent

[ 49:22 ] generates its draft of like, yeah, I think I need to return this information. Well, whenever it gets to the final step

[ 49:28 ] and it goes, okay, here's my raw data. I'm going to try and, you know, basically change it to fit this output schema. If it doesn't able, if it's not

[ 49:35 ] able to make that match, things will just fail and it's going to say, hey, I was unable to generate this output schema and things just crash. So the

[ 49:41 ] better job you can do when defining the output schema in here, the more likely your agents will do at succeeding at

[ 49:46 ] generating this this information properly. Okay, cool. So that was super important to note. Now let's just

[ 49:51 ] quickly look at the instructions and then we're going to run it so you can see how I was talking about state earlier with output keys. Yes, state

[ 49:58 ] with output keys. You're going to see how the email we generate actually gets saved to state using the email as the

[ 50:04 ] word the keyword and you're going to see the email it generates as the value. So, you'll see this in action in just a second, but let's quickly look at the

[ 50:10 ] instructions so you can see exactly what we're doing. We're saying, "Hey, you are an email generation assistant. You

[ 50:15 ] always write professional emails based on the user's request, and here are some guidelines when you're writing a email.

[ 50:21 ] You need to make sure that you always create a concise and relevant subject line. And then the body of the email

[ 50:26 ] needs to be pretty professional with a greeting. And then finally, what you want to do is make sure the tone is

[ 50:32 ] businessfriendly, formal, keep it concise, but complete. And then as we said earlier as a must, please, please,

[ 50:38 ] please make sure you include the JSON structure for best results. Okay, great. That's everything that we need to do. So

[ 50:45 ] let's run the agent so we can see this in action. So we are in the proper folder structured outputs. We have our

[ 50:51 ] virtual environment created. So we can now run ADK web. This is going to spin up our website that you normally see.

[ 50:57 ] And I'm super excited to show you guys this in action because as you build your own agents, you will see quickly how

[ 51:04 ] powerful and how important this is in order to build bigger, more complex workflows. So we can say, "Hey, please

[ 51:11 ] write a email to my wife

[ 51:16 ] Carly to see if she is available for coffee tomorrow morning." So what it's

[ 51:24 ] going to do is take in that input that we gave it and you can see the agent returned the two pieces of information

[ 51:31 ] we wanted the subject it also returned the body cuz that's exactly what we defined in the schema. Now digging even

[ 51:38 ] deeper you can see inside a state we now are saving the email we generated in the

[ 51:44 ] exact format that we said. So in our case, we said, "Hey, I would like you to save the email using the key email and

[ 51:52 ] then the body like whatever response you generate, you need to save it in here." And the reason we can see this is

[ 51:57 ] because if you hop back over here at our agent, you can see, yep, the output key was email. It's right here. And then the

[ 52:05 ] generated result is spit out right here. Now, just to show you guys something else is if we were to write another

[ 52:11 ] email, it will override this state. So you can say great see great we'll say

[ 52:17 ] write another email to see if Nate is free for pickle

[ 52:24 ] ball tomorrow night. Now this will create another email and it will save

[ 52:30 ] the result once again to state. So you can see new subject line new body but

[ 52:35 ] it's all saved under the same key. So that is working with structured outputs in a nutshell to where you now have

[ 52:41 ] total control of making sure your agents always generate the proper output schema and save the information exactly where

[ 52:47 ] you want in state so other agents can use it or you can pass that information over to other tools and APIs. So that

[ 52:53 ] one was a little bit more complex. Hopefully the explanation made sense. And now we're going to move over towards

[ 52:59 ] our next example where we are going to start to look at some of the core underlying pieces and concepts inside of

[ 53:06 ] ADK which are going to be session and memory. So let's hop over to example number five. So welcome to example

Example 5: Session, State, & Runner
[ 53:13 ] number five where we're now going to look at some of the core components you need to use in order to run your agents.

[ 53:19 ] So in this example we're going to look at sessions, state, and runners. And to

[ 53:24 ] make this all super easy to digest, what we're going to do is break this up into three phases. Part one, we're going to

[ 53:29 ] hop over to a whiteboard so you can see how all these core components work together and what they do so you have a

[ 53:35 ] good understanding of it. And once we have a highle understanding of what these components are, we're going to dive into code in phase two where you're

[ 53:42 ] going to see, okay, I understand what a runner is now, but how do I actually create it in code? Well, that's what we're going to be doing in phase two.

[ 53:48 ] And then part three, we're going to kick off the code that we run so you can see how it actually works and so you can

[ 53:53 ] see, you know, some of the outputs of everything running together. So let's go ahead and hop over to the whiteboard so

[ 53:58 ] we can deep dive into some of these core components. So welcome to the whiteboard time, guys, where we're going to start

[ 54:03 ] diving deep into understanding what is session, state, and runners and how do they all work together. And the good

[ 54:09 ] news is you've already been using each one of these different technologies and core concepts whenever you've been

[ 54:14 ] running ADK web. So far, every time we run ADK web, it handled all the complexity of spinning up all the

[ 54:20 ] back-end code that created sessions for us. So, as you can see, you know, every time we were working and chatting with

[ 54:26 ] our agent, it created a unique session for us. We'll explain that more in just a little bit. You can also see that it

[ 54:31 ] had state for us. And then every time we were chatting with our agent, we were really passing our inputs and questions

[ 54:38 ] over to a runner who was connecting everything together for us. So, enough like highle talk. Let's actually see

[ 54:44 ] what these different components are. And what I would like to do first is talk about sessions. Once we talk about

[ 54:49 ] sessions, we're then going to talk about runners. So you can see how these different core concepts work together.

[ 54:54 ] Okay. So a session inside of ADK is nothing more than really two major

[ 55:01 ] pieces of information. A session has a state. So a state is where you can store

[ 55:06 ] all sorts of information in a dictionary where you have keys and values. So keys

[ 55:11 ] could be like username and the value of username would be Brandon. So that's what we're storing in state. Outside of

[ 55:17 ] that, inside of a session, we have events. And think of events normally just like a message history between us

[ 55:24 ] and the agent. But there's actually a little bit more to it than just messages. There is also tool calling and

[ 55:31 ] agent responses. And the event history is just a list of everything that

[ 55:36 ] happens between us and the agents. And it's a nice way to store all the information so that every time we add a

[ 55:43 ] new message to the bottom, it can look back at everything we said so far and understand, oh, okay, I see we've been

[ 55:49 ] talking about this topic. So, if you ask for more information, you want me to provide more information on the

[ 55:54 ] conversation we were just talking about. So, sessions at a high level so far, state and events where events are

[ 56:00 ] messages between us and the agent. Outside of that, sessions have a few additional pieces of information.

[ 56:07 ] sessions have ids, app names, user ID, and last update time. So, let's talk

[ 56:12 ] about what each one of these is at a high level really quickly. So, as you begin to build larger agent workflows,

[ 56:18 ] you eventually we want to be able to look up sessions. So, you'll want to say, "Oh, for user Bob, I want to see

[ 56:25 ] all the different conversations he's had between him and the agents that we've

[ 56:30 ] created." And in order to look that up, what we'd want to do is go, "Oh, okay. I'm working in this app and I'm trying

[ 56:36 ] to look up the conversation that user Bob had with it. Oh, okay. By looking up that information, I can see Bob was in

[ 56:44 ] session 123. So now I can easily pull out that session and allow Bob to continue to chat with that session. So

[ 56:52 ] think of think of sessions really as just a stateful chat history. That is the best way to think of sessions. Okay,

[ 56:58 ] so that's sessions at a high level. Now to uh add in a little bit of complexity there are multiple types of sessions. So

[ 57:05 ] there is in-memory session which is where we are saving all the conversation histories that we're having with each

[ 57:12 ] one of our agents and we're saving in memory which means as soon as we close out of the application everything in

[ 57:18 ] memory is gone and we lose access to all the conversations that we had. The next option is to do a database session and

[ 57:24 ] we're going to do database session in example six the example right after this. But basically, every time we have

[ 57:30 ] a conversation with our agent, we're going to store it to a database, which is nice because when we close out of the application, all the information is

[ 57:36 ] still saved. And when we reload the application, it'll go, "Oh, great. I can pull out all the existing conversations

[ 57:42 ] between Bob, all the our other users, I can pull them out." And that way, whenever they want to continue the conversation, they can. Then what the

[ 57:49 ] third option you can do is to save these sessions to Vertex AI. Vertex AI is

[ 57:56 ] Google Cloud's AI platform. It is amazing. I actually have an entire tutorial teaching you how to deploy your

[ 58:01 ] agents to App Engine on Vert.Ex AI. But just know if you want to store your sessions in the cloud and not on your

[ 58:08 ] local computer, Vert.Ex AI is the easiest way to do it. It's out of the scope for this tutorial. And but I just

[ 58:13 ] want you to know you have multiple options. Save it in memory to where it goes away. Save it to a database to where you get to keep it on your local

[ 58:19 ] computer or option three, save it to the cloud with Vert.Ex AI. Okay, great. So we've seen sessions at a high level. I

[ 58:27 ] want to show you what a code snippet looks like of creating a session. So, as we decided just a second ago, you have

[ 58:33 ] to pick where do you want to save your sessions. So, we are going to import our sessions and use the in-memory one cuz

[ 58:39 ] we're not trying to connect it to anywhere fancy right now. So, we're going to say all right, I would like a in-memory session. And then what we can

[ 58:45 ] do from there is go I would like to create a session because I want to be able in this case my example user to be

[ 58:53 ] able to begin talking with my agents. And then you can pass in some additional information like the app name. It is

[ 58:59 ] required but just know you know we're we're not really building apps right now. We're just mostly focused on talking with our agents. So yeah just

[ 59:06 ] know you have to give an app name. You have to give it a user ID. And then from there the other option you have is to

[ 59:11 ] give state. State is optional, but this is where you can pass in all sorts of user preferences or whatever agentic

[ 59:18 ] workflow you're building. It's usually helpful to build pass in state to allow the agent to have some additional

[ 59:23 ] context instead of just the instructions we give it. Okay. Then once you create a

[ 59:28 ] session, what you can see is when you log what's in the example session, you

[ 59:33 ] can see it has all of the different properties that we called out right here. So we have an ID, the application

[ 59:38 ] name, the user ID, state. We have events which were nothing more than the events

[ 59:44 ] between us and the agent, specifically the messages, tool calls, and agent responses. That's what you're going to

[ 59:50 ] see inside the event list. And then finally, every time we make a request, it also updates the last update time. So

[ 59:56 ] you can just see like, oh yeah, we've been using this agent super recently, or no, we haven't touched this agent in a week. Okay, great. So that's session at

1:00:03
a high level. And just the core takeaway from this is sessions are just stateful message histories. That's the core thing
1:00:09
to take away from this. Okay, great. So now we're going to hop over to well now
1:00:15
that I know what a session is, how do we actually like get agents to run? Like there's a lot of moving parts. How do they all connect? Well, everything
1:00:22
connects inside of a runner. And a runner is I'm going to walk you through what you need to provide to a runner
1:00:28
first and then we're going to go through an example life cycle. So a runner is nothing more than a collection of two
1:00:34
pieces of information. Your agents and your sessions. So let's walk through why
1:00:40
we have to put this in an agent or inside of a runner. So inside of a runner, we need to give it agents so
1:00:45
that the runner knows every time it gets a request. Well, what agents do I have available to take and handle this
1:00:52
request? For example, if we were working with a frequently asked question agent,
1:00:57
well, we would see, oh, okay, I have a a question and answer agent. So, every time I get a request, I know I can give
1:01:04
it to that agent to to be the starting point to handle answering the question. Also, we need to have a session because,
1:01:10
as we just discussed a second ago, we need to have somewhere to store our message history and our state. So, these
1:01:16
are the core components that you need in order to create a runner. So, let's walk through a quick example of how us
1:01:23
chatting with the runner actually works step by step. So, let's say going back to our frequently asked question agent,
1:01:30
let's walk through it. So, let's say our user says, "Hey, what is my name?" Or we
1:01:35
can say, "Hey, what is the return policy for this business?" We'll go with that example. Well, first thing that it's
1:01:42
going to do is the runner is going to go, "Okay, you are user Brandon and I
1:01:47
can see you are asking this question." So, first thing I'm going to do is look through our session. I can see you have
1:01:53
a user ID of 1 2 3. So, I'm going to look through all the sessions I have available and I'm going to see, okay, I
1:01:59
see you have a message history and you are currently have this state. Great. From there, it's going to pass over all
1:02:06
the context it provides and finds to an agent. And this FAQ agent is going to
1:02:12
go, okay, I can see user Brandon likes these things. He's purchased these products from us. And now that I'm
1:02:18
working with the frequently asked question agent, I can now begin to generate a response. And this agent is
1:02:24
going to go, okay, in my workflow, I am a single agent. I don't have five sub
1:02:29
agents, something we'll talk later about more later on, but I can see that I have one agent. So I am now trying to figure
1:02:36
out which agent is going to handle this response. And since there is only one agent in here, I'm going to pass the
1:02:41
query you gave me plus all the session information I have about you to the agent who's responsible for handling
1:02:48
this request. In this case, there's only one agent. So that's the agent that gets picked. From there, that agent makes a
1:02:54
few extra calls. If we have tools provided to the agent, the agent will go off and maybe search the internet. It
1:03:00
might go off and search our database. Whatever we need to do, it will make the necessary tool calls. And then from
1:03:06
there it'll pass in an a request over to our large language model. So Gemini. So
1:03:11
it's going to pass the results from the tool call into the large language model and go, "Oh, okay. I can see you were
1:03:17
trying to make a request about our return policy. I can see you've ordered this product. Yep. I looked it up. It
1:03:23
looks great. It looks like you can return that item within 30 days and it's only been 20. So you can return that
1:03:30
item." From there, what'll happen is on the way back to the user, we will update
1:03:36
our session by adding in new events because if you remember from above, sessions have two pieces of information.
1:03:43
They have state and they have events. And these events can also include the agent response. So, we're going to add
1:03:49
in the agent response where we're going to say, "Yep, you can return the item you're talking about." So, that's us
1:03:56
updating session. And then finally, the runner is going to spit back the result to the user and say, "Yep, looks good.
1:04:02
You can return the item. Everything's happy." So this is the core loop in a nutshell of working with basically all
1:04:10
the core concepts we just talked about, which are going to be runners, sessions, and state. So hopefully that makes
1:04:16
sense. The core lesson here is sessions. Just one more time, sessions are stateful message histories and runner is
1:04:22
nothing more than just a combination of all the raw ingredients needed to generate responses for our users. And
1:04:29
when I say raw ingredients, just a list of our agents and the current session we're working with. It combines them
1:04:35
together to help generate intelligent responses. So hopefully that all makes sense. And don't worry, we're going to
1:04:41
dive into a code example next so you can see all of these different core components working together so you can
1:04:46
see them in action. So, let's go ahead and hop over to the code so you can see everything running. So, now it's time to
1:04:51
look at the code when it comes to combining all of our session, state, and runners into one area so we can begin to
1:04:57
chat with our agents. And the core takeaway that I want you to have inside of this code example is we are having to
1:05:03
build all the core functionality that ADK web command normally handles for us.
1:05:08
We're having to build it here. And this is super important as you want to go off and create more complex agents where you
1:05:15
don't want to just chat with them inside ADK web. Let's say you want to start incorporating agents inside of your
1:05:21
applications. This is how you would go about doing it where you would yourself manage the memory, the sessions and the
1:05:28
runners. This is what you would be responsible for doing in your own applications. So let's go through this part by part where I'm going to explain
1:05:34
everything that's happening so you can you know hopefully master everything as well. Okay. So what are we doing first?
1:05:39
Well, first thing we're going to do is we are going to load our environment variables. The reason why is inside of
1:05:46
all of our other projects, we would keep our environment variables with our agents. But now that we're managing
1:05:53
everything ourselves, we need to keep our environment variables at the root level of our folder because we're not
1:05:59
running ADK web, which is going to handle and pull out all the environment variables inside of our agents. The environment variables now need to leave
1:06:05
live at the top level of our folders. And per usual, our environment variables just have our API key and everything
1:06:12
else that we need to make requests. Okay, great. So now let's start looking at some of the core concepts that we are
1:06:17
trying to do here. So the first thing that we decided is we need to pick which memory service we're going to use. We
1:06:24
can do database inmemory or vertex AI. We just want to run everything locally for this example so you can get a you
1:06:31
know a quick overview of seeing this in action. So we're going to create an in-memory service where the second we
1:06:36
close the application all of our sessions disappear. Okay. The next thing that we are going to do is we are going
1:06:43
to create initial state. As I said earlier initial state is nothing more than a dictionary. So you can see we are
1:06:50
creating a dictionary right here and we are giving it two keys. We are giving it a username and user preferences. These
1:06:57
are the two different keys we are passing in our dictionary. So we can ideally in this frequently asked
1:07:03
question agent called Brandonbot what we can do is answer questions about Brandon. That's what we're trying to do
1:07:09
here. So that's why we want to pass in initial state. Great. So now we are going to create a session. And if you
1:07:16
remember what you have to do is inside of whatever memory service you pick, you can then say I'd like to create a
1:07:22
session using this service, this session service. So in our case, we need to create a session and pass in all the
1:07:28
values necessary in order to create it. You saw this just a second ago when we were looking at the Google example, but
1:07:34
you can see we need to pass in the app name. In our case, Brandonbot. From there, we need to come up with a user
1:07:40
ID. We're just going to call it Brandon Hancock. And then we need to pass in a session ID. And we're just going to do
1:07:47
this right here which is called a universal uniquely identifiable key basically which is just it's just going
1:07:54
to make a super long random character that you know are very unique. And then finally what we're going to do in our
1:08:00
session is we are going to provide initial state. So that's everything you need to do to create a session. Awesome.
1:08:06
So now that we've created our session what we're trying to do is if you remember when it comes to raw ingredients to making a runner there was
1:08:13
two. For a runner, we need to have in our case, we need to have our agent and
1:08:18
then we need to have our session. So, we just created our session check. And the
1:08:23
next thing we need to do is pass in our agents. So, where the heck do our agents live? Well, in our case, we've created a
1:08:30
folder where our questionans answering agent lives. So, you can see it's all in the same folder. And if you open up your
1:08:37
questionans answering agent folder, you can see it looks just like the rest of them. And if you open up agent.py, Pi,
1:08:43
you can see, hey, you are a helpful assistant and the job of you as a helpful assistant is just to answer
1:08:49
questions about the user's preferences. And this is where we're starting to get a little fancy because in order for you
1:08:55
to access state, you can use begin to use it's called string interpolation,
1:09:00
which is really just a fancy word for putting the key you want inside of brackets. So going back, let's do a side
1:09:07
by side so you can see it. So inside of our basic session right here you can see
1:09:13
in our initial state we had items such as our basically our username and you
1:09:19
can see that right here we can access our username. So this is how you access state inside of your agents. You just
1:09:27
pass in the key that you want from over here and you can pass it in here. So that is how you can access state inside
1:09:33
of your agents. super helpful and you're going to do it a ton as you work more and more with your agents. Okay, great.
1:09:38
So, now that we understand what the agent can do, let's hop back over to our runner because our runner was
1:09:44
responsible for taking in our agent that I just showed you and responsible for taking in our session service because
1:09:51
once it has those two core pieces of information, we can now begin to ask questions and send in messages to our
1:09:58
runner. Now in order to create a message the raw way to do it inside of ADK is to
1:10:03
create a message that looks just like this where you say hey I would like to make a message and the way you do that
1:10:09
is through there's a library called types. So from Google's generative AI
1:10:14
library that you have installed inside of whenever we created our Python environment. What we did is uh we
1:10:21
imported generative AI from Google. Now what we can do is create a new piece of content which is basically just a
1:10:26
message is the best way I like to think of it. And with a content, you want to pass in two pieces of information. The
1:10:31
role. So the role is going to be either the user or the agent. So who's responsible for sending this message,
1:10:38
role or user. And then from there, you have parts. Think of parts just as the raw piece of text that you want to pass
1:10:44
over to the agent as your query. In this case, we're going to say, "Hey, what is Brandon's favorite TV show?" This is the
1:10:50
message we want to send to the agent. So what we can do is go all right now that I have everything set up and ready to
1:10:57
run I can say all right runner I would like you to run everything that I've given you so far for the user ID and the
1:11:06
session ID and I would like you to process this new message. From there the
1:11:11
runner is going to go off and process everything that we just talked about in
1:11:16
the life cycle earlier where it's going to look at the agents it has available. It's going to pull information from state by looking through our sessions.
1:11:23
Pass all that information over to the relevant agent. There's only one this time. So, it's just going to pass all that context to that one agent. That
1:11:30
agent is then going to say, "Hey, do I have any tools I can call?" Nope, I don't. So, all I'm going to do is pass
1:11:36
all this information over to the Gemini LLM. And the reason I say Gemini LLM is
1:11:41
because that's the only LLM that we have attached to this agent. From there, it's going to generate a response. And that
1:11:48
response is going to get saved as an event to our session. So that's why we are going to look through our session
1:11:55
and say, is this the final response from this run? If it is, what I would like you to do is please show me the content
1:12:02
from this final event so I can log it so I can see it. And if you remember earlier, every event, that's what we're
1:12:09
looking at. An event has content. That's why this is like type.content. So, we're just basically in short, in summary,
1:12:16
just looking for the message that was responded and sent back by the agent. So, that was a lot of talking. What I
1:12:23
would like to do is run this for you guys so you can see it in action. So, let's go ahead and run this. So, let's
1:12:28
clean things up. And a few things. First off, we need to make sure that you are in example number five and you do have
1:12:35
your current Python environment activated. And what you can do now is run Python and then run basic stateful
1:12:41
session. And if you remember what this is trying to do is it's going to answer the question, what is Brandon's favorite
1:12:47
TV show? And then we are going to log two pieces of information. We are going to first log the final response. Then we
1:12:55
are going to grab the current session and we are going to show the session state. That's what we're trying to do in
1:13:00
this quick example. So you can see everything working together. So, it takes a second to run and you can see
1:13:06
great, we created a new session with a unique session ID and you can see it
1:13:11
answered the question super easily because it looked through the state we passed in. So, you can see, oh yeah, Brandon's favorite TV show is Game of
1:13:18
Thrones currently re-watching it as we speak. From there, what you can see is we're doing a session event exploration
1:13:24
where we're just trying to look at the final state. And once again, you can see this initial state that we passed in.
1:13:30
You can see that we have access to all of it right here. And this is how it was able to answer the question of what is
1:13:35
Brandon's favorite TV show. So yeah, that is sessions, state, and runners in
1:13:41
a nutshell. This was definitely a little bit more codeheavy than running ADK web,
1:13:46
but these are the core components you need to run your agents, especially if you want to start adding them over to
1:13:52
your applications and you know, in order to run your agents. So, what we're going to look at next is we're going to head
1:13:58
over to example six. So, you can see how we can connect up our sessions to a
1:14:03
database. So, it doesn't matter when we close out of the application. When we reopen it, we're going to have access to all of our sessions. Let's go over to
1:14:10
example number six. Hey guys, and welcome to example number six, where you're going to learn how to store your
Example 6: Persistent Storage
1:14:16
sessions and state to a local database so that when you close out of your application and reopen it, it's going to
1:14:22
be able to pull in all that existing information and you're going to be able to pick up the conversation right where you left it off. And in this example,
1:14:29
we're going to break it down into two parts. First, we're going to review the entire code part by part so you can
1:14:34
understand exactly how we can pull out existing sessions, how we can save sessions to a database. We're going to
1:14:40
cover everything step by step. And then part two, we're going to run the example so you can see everything in action. And
1:14:47
this is by far one of my favorite examples in the whole crash course because this is where everything should
1:14:52
click and you go, "Oh, I now understand how everything works together." And as a quick note, if you haven't watched the
1:14:58
beginning of example number five where I break down the core components of sessions, state, and runners, definitely
1:15:04
recommend checking that out again before watching this one. But without further ado, let's go ahead and hop over to the code. So now it's time to look at the
1:15:11
code for how we can start to save our sessions to a database. So when we close out of an application and restart it, we
1:15:18
can still access all of our previous messages. Okay, so let's walk through the five different highle parts of this
1:15:24
code so that we can be on the same page. So first things first, our whole goal is we want to begin to save sessions to a
1:15:30
database. So what we need to do is we need to say hey I would like to save all
1:15:36
my sessions to a specific database file. In this case we're saying I would like to save it to a SQLite file which is
1:15:44
basically just a SQL database that's just super easy to work with. And I want the file to be called my agent data
1:15:51
database. Now you can see over here in our folder structure I already have an existing database. So you can see
1:15:57
whenever we run this code in just a little bit, it's going to create a database file just like this inside of
1:16:03
example number six. So that's what it's going to do. Now we can say, all right, when it comes to which sessions I would
1:16:09
like to use, well, if you remember in the last example, we were using the inmemory session service. Well, this
1:16:15
time we're using the database session service. And quick pro tip, you can save these sessions locally, like these
1:16:22
database sessions locally, or if you have a database running in the cloud somewhere hosted like on Google Cloud
1:16:28
Platform or another database hosting services, you could point it there as well. But for this example, we're just
1:16:34
saving everything locally. All right. Next, what we want to do is define some initial state because what we are trying
1:16:39
to do in this example is to create a reminder agent who will take in reminders from us, save these reminders
1:16:46
to a list and then when we are done with those reminders, it should remove the reminders from our list. That's exactly
1:16:52
what we're trying to build inside this agentic workflow. So, we need to update our initial state to say our name and
1:16:58
start off with a blank empty list of reminders. From there, what we're trying to do is begin the process of working
1:17:06
with existing sessions and creating new ones. So, imagine if we start creating a new conversation with our agents and
1:17:13
it's the first time we're working with them, it should create a new session. If it is the, you know, we've been talking
1:17:19
to this agent over and over and over, we should pull out our existing session. So, let me show you how we're doing this. Well, first things first, we need
1:17:26
to give our app an application and pass in a user ID. So, we need to have these.
1:17:31
And then with inside of our session service, which is going to be our database session service that stored all
1:17:37
of our previous conversations in this file, we're going to run the command list sessions. And what this will do is
1:17:44
it will look up for this specific application and this specific user. It will look up all existing sessions that
1:17:50
we've already had with this agent. From there, we're going to do a quick check. So in option number one, we're going to
1:17:57
say, hey, did this existing session already exist? And does it have a length over zero? Meaning like there's there is
1:18:04
a session because obviously if there if it exists, the number will be one and greater than zero. And if that's the
1:18:10
case, what we're going to do is pull out the session ID from that existing session. So that's how we're going to
1:18:15
get our session ID. If this is the first time we've began to chat with this session, what we want to do instead of
1:18:22
using the existing one is we want to create a new session. And if that's the case, what we want to do is pass in the
1:18:29
app name, the user ID, and initial state. So either way, we're going to be in a great situation where we have a
1:18:35
session ID that we can begin to communicate with. Great. So now that we have that session ID, what we can do is
1:18:42
begin to start to set up our runner just like we did in example number five. And if you remember the core ingredients of
1:18:47
a runner was our agent who's going to be responsible for handling all the requests and has all the instructions
1:18:53
and tools and agents everything inside of it. So we want to pass in the root agent and we also need to pass in the
1:18:59
specific session service that we've been working with. So in our case remember the session service is nothing more than
1:19:05
the initial database session service that we set up from the get- go. Okay great. So now that we have our runner
1:19:12
set up, we are set up to start a interactive conversation loop. And this is where we are going to go through the
1:19:19
following where we are going to work with a memory agent chat that will remember reminders for us. And whenever
1:19:24
we're done chatting with it, we can type in exit or quit and it will kill the conversation for us. So what I would
1:19:30
like to do is do a quick run through of this and actually run the agent so you
1:19:35
can see in action. And two things I want to do before running it is I want to go clean things up. So, I want to delete
1:19:41
our database so that we're running from a clean slate. So, we're deleting the database. And then I want to show you
1:19:48
how we're handling each request. So, each user input that we get when we're chatting with it, I want to show you how
1:19:53
we handle it. And that's all inside of the call agent async function. I put this in a separate file called
1:19:59
utils.py. So, you'll notice in the example 6 folder, I have a utils.py file
1:20:05
for you. And this has a few different functions to help make your life simpler. And we as good programmers want
1:20:11
to keep our code clean in our main file. So let's walk through this really quickly so you can understand what's going on. So first things first, we're
1:20:18
passing in a few different pieces of information. We're passing in the runner that has access to our sessions and it
1:20:25
has access to our agent. From there, we want to pass in the user ID. So who's making the request in which session are
1:20:31
we working with? And then finally, we want to pass in the raw query, which is like, oh, what did Brandon ask? From
1:20:37
there, we need to convert the query we get into a piece of content. And if you remember from example five, a content is
1:20:44
nothing more than just a message we want to send over to our agent. From there, what we're going to do is log it. And I
1:20:52
have set up a bunch of print statements to make our lives a lot easier so we can inspect what's going on. You'll see this
1:20:58
in just a second when we run it. But the core thing that you'll notice is once again we are going to for that runner
1:21:03
we're going to call run. Last time we did runner.run and this time we're going to do runner.async. Google ADK
1:21:09
recommends to always use runner async and to only use runner.run when you're testing locally.
1:21:16
So if you're doing any real world application always use run async. Now once we have that set up for our runner
1:21:22
we pass in all the information that we've been working with. So who's making the call? What are the previous messages
1:21:28
that we have been using and talking about with this specific user and between them and the agent? And then
1:21:33
finally, what is the new message that you want me to work on? From there, the runner is going to go through that life
1:21:38
cycle that we talked about last time and we are going to process the agent response. So, let me show you what that
1:21:44
looks like. And basically, what we're going to do is iterate through all the different pieces of content that we get.
1:21:51
And what the main thing that you want to care about is we're going to log the final response. So if it is the final
1:21:58
response, we're going to log it. And so you can see, oh yeah, this is what the agent said. Don't worry, it doesn't
1:22:04
matter. A lot of this complex code is all around just printing statements. So you don't really need to to worry about
1:22:09
a lot of it. Okay, great. So once we process the agent response and we have it, we log the final response text right
1:22:16
here. So we just return the final response. So that's it in a nutshell. I know that was a little bit more complicated, but don't worry. I'm going
1:22:22
to run it and it will all make sense. So, let's clear everything out and run the agent so you can see it all in
1:22:28
action. And we're going to do two different runs. The first run, we're going to start out with a blank database
1:22:33
where it doesn't exist. So, we're going to have ADK create the database file for us. Then, we're going to ask a question
1:22:39
or two, create a reminders, and then we're going to close out of the application and restart it so you can see everything in action. So, let's
1:22:46
start the fun. So, we are going to inside of file 6 with our virtual environment activated, we are going to
1:22:51
run python main.py. And this will allow us to uh it'll spin everything up. In
1:22:57
just a second, we should see it created a database file for us. From there, we can now start to add reminders. And I'm
1:23:04
going to make this really big so you can see what's going on. So, we're going to say, "Hey, please set a reminder for me
1:23:14
to take out the trash tomorrow at 5:00
1:23:19
p.m." From there, the agent is going to take in that request. And from there,
1:23:25
the agent is going to respond, "I've added your reminder to take out the trash tomorrow at 5:00 p.m." And yeah,
1:23:30
so that's what it's saying. And now, as an extra bonus for you guys, I log the
1:23:35
state before and after every request. So, you can see the state before processing this message was none. We had
1:23:42
zero reminders, but afterwards, the agent created a new reminder for us.
1:23:48
Now, how the heck did it do this? How did this agent save a reminder? Well, we
1:23:53
didn't fully show this off initially, but if you go to your agent.py pi file. You can see we created I'm going to
1:23:59
minimize these so you can see in action. One second. So what you can see is we now have a new memory agent. This memory
1:24:08
agent takes in a few core pieces of information. It has a description and it
1:24:13
has instructions. And when it comes to instructions, we say, "Hey, you're a friendly reminder assistant. You are
1:24:18
working with this shared state information. Specifically, you have access to the person's username and a
1:24:23
list of reminders. From there, what I want you to do is you have the following capabilities. You can add new reminders,
1:24:29
view existing, update them, delete them, or update the user's username. From there, I give it some extra specific
1:24:35
instructions telling it how it should handle the process. The basic CRUD, which stands for create, read, update,
1:24:41
and delete. I walk it through the basic operations for creating and working with updating our our different reminders.
1:24:48
Now, how do we actually update state and our reminders? Well, the way we do that
1:24:53
is through our tools. So, we have added multiple tools to this agent. So,
1:24:59
everything from adding, viewing, updating, deleting, and the basic CRUD operations. So, that's why we have all
1:25:05
these tools up here. Now, later on when we get to tool context management, we'll work on this more. But the main thing I
1:25:12
want you to know is when you are working with state inside of your tool calls, which we'll touch on a lot more when we
1:25:18
get to callbacks, what you'll notice is there is this new tool context parameter that we give to tools. Now, what the
1:25:24
heck does this mean? Well, basically what's going on is you can pass in whatever parameters you want that you would normally give to a tool and then
1:25:31
at the very very end you can pass in tool context and tool context will have access to all sorts of different
1:25:38
attributes and specifically it's going to have access to the state. So it has
1:25:43
access to all sorts of information. So what we're doing is we're going hey tool context I would like you to give me
1:25:51
access to the current state object and I would like you to get all the current reminders. Once I have access to the
1:25:57
reminders I would like you to add a new reminder to the list. Once I have that new reminder I want to save it back to
1:26:04
state. So this is how you add information to state. You just call state have the key and then pass in the
1:26:10
new value. And then from there, what we're doing with our tool call, cuz earlier in our example number two, when
1:26:15
we learned about tools, you learned that you want to make sure your tool return statements are as informative as
1:26:21
possible. So in our case, we're returning the fact the action. We're passing back the reminder, and we're
1:26:28
passing back a message saying, "Hey, I successfully added this reminder." And this is the exact same flow we follow
1:26:33
for all of our different tool calls. So when it comes to viewing our reminders, all we need to do is inside a tool
1:26:40
context, we just need to access the tool state. We want to get reminders and then
1:26:46
return them. And it's the exact same thing for all the rest of the different tools. We just pass in some variables,
1:26:52
pass in the tool context, pull out what we need, and then save it back to state. So that's exactly what's going on. So
1:26:58
we've kind of gone a little bit in the weeds, but what I want to do is add in one more reminder. Then we're going to
1:27:03
close out of the application, rerun it. So you can see that yes, it is properly saving things to our database. So let's
1:27:09
also say also remind me to mow the grass
1:27:15
this weekend. From there, it's going to update and add a new reminder using those tools that you just saw. So life's
1:27:22
good. So what we're going to do now is we are going to kill the application. So you can do that just by typing quit.
1:27:28
This will end the conversation. Life's good. Your data has already been saved to the database. We didn't have to do
1:27:33
anything extra. ADK new by providing that initial sorry let me minimize this
1:27:38
for you guys. ADK new by providing in that initial database service it would
1:27:44
automatically save everything to the database. So let's have some fun and see what was saved to our database. So when
1:27:49
you click in the database if you're using cursor you should be able to see a database viewer just like this. And what
1:27:55
you can see is it saved all sorts of information to session. It saved app state, raw events, sessions, and user
1:28:03
state. So if I open up sessions and double click on it, you can see that we
1:28:08
have a session state between the user AI with Brandon. We have a session ID and
1:28:13
you can see the state of where we left off. And if you look in the state right now, you can see it includes everything
1:28:20
that we just added a second ago. So my username and the list of reminders, which are take out the trash and mow the
1:28:26
grass. So you can see it's all being saved to a database now. And if you want as well, you can click inside of events
1:28:32
and you can see all of the raw events that happened inside of your application. As you get larger
1:28:38
applications, it wouldn't just show for a specific user, it would show for all users. So this is a really nice way to
1:28:44
see what's happening inside of your agentic workflows. And like we talked about earlier, there are two different
1:28:49
types of messages. And in this case, there are, you know, agent messages and
1:28:54
then user messages. If we and we should also probably start to see some tool calls. Yep. Just like this. So you can
1:29:00
see some messages like a user request from me which is hey please do this. You
1:29:05
can see that it involves a function call which is hey please go save. If we just click in it you can see it's calling
1:29:12
doing a function call to the add reminder function and from there it's
1:29:18
passing in the raw text of what the tool needs to do. From there you can see the
1:29:23
function response included the exact response that we wanted. So the function response now includes that message we
1:29:31
said that was very verbose which included the raw action. It included the renew reminder and a message about the
1:29:38
action that just occurred. So you can see this is all getting saved to a database. All around absolutely love it.
1:29:43
So what we're going to do next is let's close out of our database. We're going to clear things out and rerun the same
1:29:49
command. So now when we begin to talk with our memory agent again I can say
1:29:55
hey what are my current reminders. From there it's going to access our state per
1:30:02
usual and it's going to say all right Brandon here are your current reminders. And at this point it's showing the
1:30:08
reminders we already had saved to our session and which our session was saved to a database. So all around, I hope you
1:30:14
guys are like freaking out and saying like, "Oh my gosh, I now understand how everything works when it comes to
1:30:20
session. I understand what runners do. I understand how sessions can be saved to memory or to a database and kind of see
1:30:25
how it all clicks together." I know we did talk on a few additional topics like I didn't really mean to talk about tool
1:30:31
context, but hopefully it was helpful to see how tools can access state so you could see how we were altering the state
1:30:37
as we were starting to make tool calls with our agents. So, I know that was a little bit of a side quest, but hopefully it was super helpful to see.
1:30:43
And don't worry, as we begin to work with callbacks, you're going to see a lot more on that. Okay, great. Well,
1:30:48
give yourself a pat on the back. We are halfway done with you mastering ADK. And now we're going to move on to our next
1:30:54
example. So, I'll see you guys in the next one. Hey guys, and welcome to example number seven where we're going to look at our first multi- aent system.
Example 7: Multi-Agent
1:31:01
So excited for this one. And what we're going to do is break this up into three different parts. First, we're going to
1:31:07
head over to the whiteboard so you can understand how multi- aent systems work inside of ADK because it's completely
1:31:13
different from what you would expect to see in Crew AI or Langchain. From there, once we understand how things work,
1:31:19
we're going to look at a simple code example of our first multi- aent system. And then finally, in part three, we're
1:31:24
going to run it so you can see everything in action. So, let's go ahead and head over to the whiteboard so we can break down some of the core patterns
1:31:30
and behaviors of multi- aent and ADK. All right, so let's start investigating how the heck do multi- aent systems work
1:31:38
inside of ADK. Now, what I want to do in this first example is give you a brief overview of an example agent. So, let's
1:31:46
imagine we have a root agent because you always have to have a root agent inside
1:31:51
of your ADK setups. This root agent is usually considered the delegator or the
1:31:57
manager or usually this agent is responsible for delegating work to other agents. That's usually the entry point
1:32:03
to everything inside of your application. Now, here is where ADK is different than other frameworks compared
1:32:09
to like Crew AI and link chain. What happens inside of ADK is whenever you
1:32:15
send a request into the framework and specifically to your agent, what this
1:32:20
agent is looking to do is answer the query as quickly as possible. So, let me give you an example and then walk you
1:32:26
through why it's different than other solutions. So if you pass in a query such as, hey, what is the weather today?
1:32:33
This agent is going to look at the description of all of its sub agents and
1:32:39
figure out which one is the best suited to answer the query. Once it knows who
1:32:45
to pass the work to, the root agent is out of the picture. It delegates all the responsibilities to this sub agent who
1:32:52
takes control and handles it from there. From there, this weather agent then determines based on the query, well, it
1:32:59
determines, well, what tool calls should I make in order to answer the question.
1:33:04
So then it goes, oh, it looks like you want to know the weather today. Well, I will look up the weather in Atlanta,
1:33:10
Georgia. From there, once it gets the answer, the weather agent will then know, okay, I know the results from the
1:33:15
tool call. I can now generate a result and the weather agent will return the final response. Now this is totally
1:33:21
different than other frameworks like Crew AI because in Crew AI what normally happens is you have one task and then
1:33:29
for that task you usually have multiple agents trying to work on it. So in crew AI you would expect to see something
1:33:35
like this where you have get weather and what you would expect to see is you
1:33:41
would have multiple agents working on it. So you'd have a weather agent, you would have a research agent, and then
1:33:47
you would have someone else and together these agents would work together to
1:33:53
answer the question and collaborate to answer it. That is not the case in ADK.
1:33:58
It is all about delegation and single answers. There is no at least not yet.
1:34:04
We haven't worked on workflows, but at at a basic example of working with agents, it is all about delegating and
1:34:10
immediately answering the question. This was something that confused me a ton when I started out with ADK and I just
1:34:16
wanted to make sure you guys understand this core principle. So key takeaways, we focus on delegation inside ADK and
1:34:23
whoever is the best suited to answer the question, they get to work on it and they get to generate the result. There's
1:34:28
no multi-iterating over and over and over at the basic examples of ADK. We'll
1:34:33
get to workflows later on, but just know at a basic level there's no no looping multiple attempts. Whenever you set up
1:34:39
your basic multi-agent systems, they just answer the question as quickly as they can to get you an answer. Okay,
1:34:44
cool. Now, we need to look at some of the core limitations of working with ADK. So, whenever you create agents,
1:34:52
sometimes you want to use all the cool new built-in tools that ADK creates for
1:34:57
you. However, when you look at the documentation for working with these agents, it specifically says that, hey,
1:35:04
you cannot use built-in tools within a sub agent. This tripped me up because I was like, why doesn't this work? Why
1:35:09
doesn't this work? Well, don't worry. It is because you cannot use built-in tools with sub agents. So, for example, this
1:35:16
would break if you had a root agent who was just a general researcher agent who
1:35:22
was responsible for delegating out to uh sorry, it was a manager agent who's responsible for delegating out work. If
1:35:28
you had a random request of like, hey, what's going on in the news today? Well, this would fall under the search agent
1:35:34
and this search agent would try to call the built-in Google search tool. This would break. You're going to get a huge
1:35:40
error saying you can't do this and it's not the most clear error and you it's up to you to know that this limitation
1:35:46
exists. Now, there is a workaround to get this to work and let me steal the ball over here and walk you through it.
1:35:53
So, there is a workaround. If you did want to look up a generic search request of like, hey, what is going on in the
1:35:59
news today? What you can do is use the command agent as tool. And what this
1:36:05
will do is it will treat your agents as a tool call. So this is the only way to work around it to use if you wanted to
1:36:12
use tools like Google search in a sub agent, you have to use this agent as tool. Don't worry, you're going to see
1:36:17
this in the code in just just a second. But just know whenever you do this setup, what happens is the root agent
1:36:23
goes, "Oh, okay. Well, what I'll do because I want to look up the weather is I will or look up what's happening in
1:36:30
the news. I will call this pathway like a normal tool where I pass in parameters
1:36:36
and everything else to get an answer and then this will work. But this is just a weird workaround. If you want to use any
1:36:41
built-in tools like Google search, if you want to use the vector search AI or the code execution tool built in from
1:36:47
Google, this is the path you have to do. Now, I did mention a while ago that hey, there are a few different workarounds.
1:36:54
So if you don't want the behavior of the agents, you know, just doing a single shot where they're delegating the work
1:37:00
to let the other agents handle all the requests, what you can do is work with these different types of workflow agents
1:37:07
that we're going to cover in examples 10, 11, and 12 where we focus on parallel. I got to spell correctly for
1:37:13
this to work. Parallel agents, sequential agents, and loop agents. This is where we can start to have agents
1:37:18
take multiple attempts at solving answer. And don't worry, we're going to look at these at the very end. So, I just want to clear up a few different
1:37:24
things because multi- aent systems in ADK are different than anything else you've ever seen. But I want to go ahead
1:37:30
and walk you through the core lessons which were everything gets delegated. You cannot use built-in tools and sub
1:37:36
aents. If you do want to, you need to use the agent as tool wrapper. All
1:37:41
right, now you've seen all the highlevel lessons. Let's dive into the code so you can see everything in action. See you in
1:37:47
just a second. Okay, so now it's time for us to look at the code for our first multi- aent system. We're getting
1:37:54
advanced, guys. We've gone from a single to multiple. So, here is a brief overview before we dive in of everything
1:38:00
that's going on. So, first things first, we are creating a new agent just like we have this whole time. The name needs to
1:38:06
match our folder name because we are right now in example number seven. From there, we're going to give it a model just like we normally do. And then we
1:38:14
are going to give our agent instructions. So we're going to say hey you are a manager agent just to be very
1:38:20
clear that your job is to delegate and you always want to delegate the task to
1:38:25
the appropriate agent. Here are the different basically task you are allowed to delegate to other agents. So we're
1:38:32
saying you have two agents. The stock analysis agent and then a funny nerd agent who tells this joke. And then to
1:38:38
help give you guys some additional examples we're also providing this manager agent some tools. So, if these
1:38:45
agents can't handle it, we're going to pass it along to these tools. Now, here are the big changes that you're going to
1:38:52
notice inside of multi-agent solutions. So, the first one is we now have a sub agent property, which is a list, and we
1:39:00
can pass in additional agents in here. And as you remember from the whiteboard
1:39:05
session, anytime we answer a question, if one of these agents is fit best to do
1:39:10
the task, we pass the task over to these agents and they handle managing the response and doing all the work. Now,
1:39:17
how do we actually get these agents inside of our main root agent? Well, super easy. What we do is we import
1:39:24
these agents from our sub agent folder. So, inside our sub aent folder, this is
1:39:30
where we have pretty much everything that you would expect to see. We have our funny nerd and we have our stock
1:39:35
analyst and we have our news analyst. More on the news analyst in a second when we start to talk about agent tools.
1:39:41
But what you'll notice is inside of each of these sub agents, it's the exact same folder structure that you've seen for
1:39:47
everything so far where you have a folder. In the folder, you have an agent. That agent needs to have a name
1:39:54
that matches the name here. So, rinse and repeat. Same thing you guys have been doing this whole time. Now, what we
1:40:00
can do is look at how do you import these? Well, up top in the root of your root agent folder, you'll just import
1:40:07
from the sub agent folder, call out the package right here. So, this is the funny nerd package and we want to grab
1:40:13
the agent folder. Once we grab the the agent file, sorry, what we want to do is inside the agent file, we want to import
1:40:20
the funny nerd agent. So, that's exactly why these imports look just like they do. Okay. Now, what we're going to do,
1:40:28
just so we're on the same page, I'm going to give you a brief overview of each one of these agents and then we're
1:40:33
going to dive into the tools so you can see how this agent as tool functionality works as well. So, let's first go look
1:40:39
at our stock agent. Super straightforward agent. The important thing to note here is when it comes to
1:40:45
multi- aent systems, in order for the root agent to know what each of its sub
1:40:51
agents can do is it looks at the description. This description decides and tells the parent agent, hey, here's
1:40:58
what I can do and here's how I can help. So, if anyone asks a question around looking up stock prices or looking at
1:41:04
them over time, I can do that. That is my core functionality and I can help with it. And then this agent is has a
1:41:10
singular function where all it does is it gets a stock price for a current ticker. So, it just gets the yeah gets
1:41:16
current stock price. The other agent that we have is our funny nerd. our funny nerd. Once again, same model, same
1:41:23
name as the parent. And what it does is it says this agent tells funny nerdy
1:41:29
jokes. So anytime we want a joke, this model will get picked. And from there, the final thing that we're going to do
1:41:34
is now that you've seen these agents in action, let's quickly look at our news agent because this agent does it breaks
1:41:42
one of our rules because this agent imports one of the built-in tools from ADK. And because this agent imports
1:41:50
Google search, we can no longer call this agent as a sub agent. For example,
1:41:56
if we did this, this would break. I'll show it to you that it does break in a little bit in case you do run into the same error. But the important thing is
1:42:02
we have to wrap it as agent tool. Now, why do we have to do this and what's the difference when we do this? Well, if you
1:42:07
head over to the core docs inside of what agent development has and you look at the key differences of working with
1:42:14
sub aents, here's what's happening. Whenever you do agent as a tool, whenever the parent agent calls the
1:42:21
child agent as a tool, basically what happens is the result from agent of the child agent gets passed back to the
1:42:28
parent agent and then the parent agent uses that answer to generate a response.
1:42:34
So basically the child gets called. This child agent which is agent A in this case does all the work calls all its
1:42:40
tools in our case the built-in tool and then it returns the answer back to the parent and then the parent uses that to
1:42:45
respond. Whereas with sub agents, it does exactly like we said earlier, which is when a parent agent delegates to a
1:42:51
sub agent, the responsibility of answering is completely transferred to the child agent where agent A is out of
1:42:57
the loop going forward. So that is going back to the key principle earlier of everything gets delegated in multi- aent
1:43:03
systems. All right. So, now that you've kind of seen this in action, what is this news analyst or or sorry, you
1:43:09
already saw the news analyst and the way we use this news analyst to not break is we wrap it inside of agent tool and you
1:43:16
can import agent tool just like this. So, this is how you do it. Google ADK tools agent tool and we want to put
1:43:23
agent tool and that's how you wrap your agents to make them tools. Pretty straightforward. Okay. So, now that you've seen this at a high level, what I
1:43:29
would like to do is start to run the code. and you're going to see how it works at a high level. We're going to
1:43:35
look at events state, how it all gets updated. And then finally, what we're going to do afterwards is I'm going to
1:43:40
break the program where I'm going to not wrap this inside agent tool just so you can see the type of errors you would get
1:43:46
in case you ever accidentally make this mistake yourself. So, what are we going to do? We are going to make sure we
1:43:52
first off are in the right folder, multi- aent, and we've activated our virtual environment. Now, we're going to
1:43:57
run it. Once we run it, it's going to spin up our web interface that we've seen a thousand times that looks just
1:44:04
like this. And now what we can do is start to interface with our agents. So up in the top, let's actually make this
1:44:09
a little bit bigger for you guys. So even a little bit bigger. Great. So what you'll notice is there's only one agent
1:44:16
because our we only have one root agent. So now what we can do is say, please
1:44:21
tell me a funny joke. And what we would expect to happen is the root agent would
1:44:27
transfer over to the joke agent and the joke agent would then generate the
1:44:33
response. So here we can actually look at the series of events that triggered this. So transfer to agent, we can start
1:44:39
to see a little bit of an overview. Yeah, it's just starting to get a little bit bigger. So you what you can see is
1:44:44
the manager agent goes, okay, I have these different agents and tools at my
1:44:50
disposal. Now I've been asked to generate a funny joke. So we are going to now do it make a function call to
1:44:58
pass over this query to the funny nerd and we are going to transfer over to this agent. So if we go over to the next
1:45:05
event we should start to see that the yeah sorry if we go over to the next event you should start to see that the
1:45:10
funny nerd is now responsible for handling this request. And you can see that the funny nerd is like the code
1:45:18
told it to do is ask what it would like to to generate a joke around. So if you per usual go and look at the what the
1:45:25
code is, it put together the prompt and basically well I'm not going to go too deep into that. That's too beginner for
1:45:30
you guys. But the important thing now is you can say all right what would you like a joke about? Would you want to hear about Python, JavaScript, whatever
1:45:37
you'd like. So we'll say we'll do a joke on Python. And then now what we should see is we have quite a few more events.
1:45:43
So if we start to look at them, you can see now that we've asked to get a specific joke for a specific tool. It's
1:45:49
going to call the get nerd joke for the topic Python. And now it's going to return a nerdy joke around Python. So
1:45:57
yeah, that's exactly what it did. Okay, cool. Well, what other tools do we have access to? So let's quickly look really
1:46:03
quick and see. All right, the other one we could do is stocks. So tell me the current stock price of Microsoft because
1:46:12
it shot up today. Now what this is going to go do is oh see so now we are still currently
1:46:19
in the funny nerd joke. So what we could do is we would normally want to so now
1:46:25
that we've been delegated from the root manager to the funny nerd we are now
1:46:30
stuck with the funny nerd. So usually you can sometimes get delegated out of this. So what we can do is mention the
1:46:36
word delegate. So delegate gate to the root agent then
1:46:43
tell me the current stock price of Microsoft. Sometimes this will work. Yeah. So if you're already in an agent
1:46:49
that is like a funny nerd, it doesn't always do the best job of delegating. So sometimes you have to mention, hey, you
1:46:55
need to refer me to another agent. Now what we can do is you can now see that we were transferred from the funny nerd
1:47:02
back to the manager and once we were in the manager we eventually get transferred over to the stock analyst.
1:47:09
So what you can see now is the stock analyst called the proper tool and the tool returned the current price of
1:47:15
Microsoft which is as of today $424. This was a weird quirk. This probably
1:47:22
has happened to me one out of 10 times. Normally if an agent is over its TED it just automatically does this rerouting
1:47:29
for you. So that's probably something that we should have updated the prompt to say like hey if you get a request
1:47:36
that you are not comfortable answering delegate back to the parent. So that was just a weak prompting on my part. Now
1:47:42
what we can do so you can just see a few other things. Let's just say what is the
1:47:48
news for today. And what this should do is yeah, so we need to say delegate
1:47:54
again. So yeah, I just should have improved the prompting to say if you can't handle the request, delegate to the manager. Delegate to the manager,
1:48:02
then tell me the news. Now, this will, per usual, transfer transfer. And now
1:48:07
we're going to go over to the news analyst. The news analyst is going to use the Google search tool to find it
1:48:12
and then give me a summary of today. Okay, great. So, you've now seen how we can start to work in multi- aent
1:48:18
systems. Now, what I want to do is break things because that is fun. So, let's what we can do is get the news analyst
1:48:25
out of here. We're going to move the news analyst here just so you can see what the error would be. So, if we
1:48:31
respin up our server, what you'll notice now whenever I go to type into our
1:48:36
editor. So, if I do I'll just show you. So, I can say get the current time. So I
1:48:42
can show you it still works unless we call the the bad agent. So get the current time. So this will get the
1:48:48
current time call the tool. Everything looks great. But if I now say please look up the current news for today, this
1:48:58
will break and it'll say, "Oops, this tool is being used with function calling
1:49:03
that's unsupported." Which is a bad way of saying, "Hey, you're being silly.
1:49:08
you're trying to call a tool that you're not allowed to. So, you're trying to use an agent that is not that is supposed to
1:49:15
be wrapped in agent as tool. So, I just wanted to show you guys that because that when that broke the first time for
1:49:20
me, I was like, what's going wrong? So, I just wanted you guys to see the error. And then quick other thing I did want to
1:49:25
mention so you guys can see what I was talking about earlier. What we should have said over in our other prompts to
1:49:31
say like if the user asks about anything else, what you should say is you
1:49:39
should delegate get the task to the manager
1:49:44
agent. So if we just run it again just to show you guys all this. This is a little bit of live debugging so you get to see behind the scenes a little bit.
1:49:51
So what happens now is we'll ask to get a funny joke and then we'll ask to get the news just so you can see that it
1:49:57
does delegate properly. So we have to be hyper specific with these agents because they don't they only act on what
1:50:03
information we give them. Great. So it's up and running again. So now we can say tell me a funny joke. Now this will go
1:50:11
find a funny joke. We've been transferred over to the proper agent now which is going to be yeah the funny
1:50:17
agent. Yeah. So now we're talking with the funny nerd. And now we can say actually get me the current news for
1:50:26
today. And then now it should delegate us properly over to the proper agent. Great. So now we're getting delegated.
1:50:33
We're transferred over to the the funny. Yeah, sorry. It's it's struggling to
1:50:39
Yeah, it's ending up in a awkward loop. So we can actually kill it and sometimes
1:50:44
Yes. So it's like stuck in a loop right now going back and forth. So yeah. So sometime sometimes it is not the most reliable on delegating. So what we can
1:50:52
do because it's it's actually struggling really hard. No joke anymore. Just give
1:50:59
me the news for today. Great. So you can see now it's
1:51:05
transferring. Yeah. So it was just because it was in a weird state between the two, but now we're properly getting delegated to the news and now it's
1:51:11
there. So, long story short, what we could have done is just been more instructive inside of our agent in
1:51:17
descriptions and just said, "Hey, only answer questions. If anything ever goes wrong that you can't help, always just delegate back to the root agent." And
1:51:24
that would have solved the problem. So, hopefully you guys got to see some of the cool parts of multi- aents. You got
1:51:29
to see the limitations of why we have to use agent tool calls. You saw how we
1:51:34
could improve our agent descriptions in case anything goes wrong to say delegate to the manager agent to help with
1:51:40
delegation processes and you got to see a little bit of debugging along the way. So, what we're going to move on next is
1:51:46
we're going to hop over to working with our multi- aent solution, but we're going to now start working with shared
1:51:51
state that we are going to share between our agents just so you can see that in action. So, let's hop over to example
1:51:56
number eight. And if you have any questions on anything so far, feel free drop a comment down below and I will happily help out. Thanks, guys. Talk to
1:52:02
you in the next one. Hey guys, and welcome to example number eight where we're going to focus on building a multi- aent system that starts to
Example 8: Stateful Multi-Agent
1:52:09
interact with state. And so excited for you guys to see this one because this is where we start to add in some additional
1:52:14
complexity and really start to allow our agents to solve complex problems. And I'm so pumped for you guys to see this
1:52:20
agent workflow in action because we're going to be building a customer service agent that has multiple sub agents that
1:52:27
basically allow us to handle all customer support for a course. That's basically the demo that we're going to
1:52:33
be focusing on. So, let's break down the three different parts of this example. First things first, we're going to head
1:52:38
over to our whiteboard where we're going to break down how all these agents work together in order to handle all parts of
1:52:44
customer service for a course that we're selling. From there, after we understand the high level of what's going on, we're going to dive into the code so you can
1:52:51
see exactly how everything works together. And then finally, we're going to run this agent so you can see it in action. So, let's hop over to the
1:52:57
whiteboard so we understand what's going on and how we're going to build a multi- aent system to handle our course sales.
1:53:02
All right, so let's look at the multi- aent system that we're building that's going to help us with all sorts of
1:53:08
customer service for a course that we're selling. So, at a high level, what we're doing is we've created a customer
1:53:14
service root agent that has four different sub agents in that it can work
1:53:19
with. Now, let's do a quick overview of what each one of these agents can do. So, first things first is we have a
1:53:25
policy agent that just gives some general information about the policy for the AI developer accelerator course that
1:53:31
we're selling and it can answer all sorts of questions, refund questions, anything you know related to just
1:53:37
general questions answering that our customers might have. From there, anytime someone wants to purchase a
1:53:42
course, they're going to be directed to our sales agent. And the sales agent is there to give people a little bit of
1:53:47
information about what's in the course, get them excited about what we're doing. And then if they do want the course,
1:53:53
it's going to allow them to buy it. And when they buy it, this is where we're going to start to actually start to
1:53:59
interact with state. So whenever a customer does purchase a course, this is
1:54:04
where we are going to update the state. So let's look at what's in state first and then we're going to come back to purchase course. So at a high level what
1:54:12
we have inside a state are three different keys. So we have username so you know who's working and who we're
1:54:17
talking to. From there we have purchase course. So this is where we can see what courses the person has already accessed.
1:54:23
And a purchase course will always appear in this structure where we have the course ID. So this is going to be like
1:54:30
oh you've bought course number one or course number two. And then also the purchase date. The purchase date is
1:54:36
super important because if the person wants a refund, we can will 100% honor that if it's been less than 30 days. So,
1:54:42
let's go back to the purchase course. So, if someone does try to purchase a course, what we'll do is go, okay,
1:54:48
great. You want to buy this course? Well, what we'll do is it looks like you do not have any purchase courses in
1:54:53
state. So, I will happily buy this for you, charge you the the $150, and then from there, I will update the state so I
1:55:00
know in the future if you have any questions that you have access to this course. If we for whatever reason
1:55:06
already have access to this course, like we bought it in the past, the agent's going to go, "Oh, it looks like you already own this. You can't buy it
1:55:12
again." So, just uh we're gonna have some nice logic in our prompts to help make that happen. Now, from there, what we have is our course support agent. Our
1:55:19
course support agent always looks to see which purchase courses we've made so far
1:55:24
and then it can answer questions about them. So, for example, once you buy the course, it's going to say, "Okay, I can
1:55:31
now help you answer any questions about any of the modules inside the course." We don't want to give away too much
1:55:36
information about like what's happening in every single lesson and module inside of the course until people buy it. So,
1:55:43
that's why this agent checks to see, hey, have you bought it? If so, great. I can answer any question and help you
1:55:49
through any problem inside the course. So, this is a pretty cool one. And then finally, if people do uh want to get a
1:55:55
refund, they'll be directed over to the order agent. And the order agent has one job, which is to allow people to get
1:56:02
refunds on their courses. So, whenever someone does want a refund, what'll happen is we'll check to see if they
1:56:07
first own the course. And if they do, great. If they uh what we'll do is we will refund them, send them their money
1:56:13
back, and we will drop the purchase course from state. So, this is kind of how multi-state systems work to where
1:56:20
just a quick recap of why this is so awesome is we're now sharing state between all of our different agents and
1:56:27
depending on the state, these agents behave differently. So, quick recap. Sales agent will buy the course if it's
1:56:34
brand new. If they don't already own it, if they do own it, we'll say, "Nope, you can't buy it again." The course support
1:56:39
agent is going to go, "Hey, do you have access to this agent?" Great. I can answer questions. Do you not purchase
1:56:46
this course already? Great. I will not be able to answer those questions yet, but if you would like to purchase it,
1:56:51
great. I'll refer you over to the sales agent. And then finally, the order agent will say, "Hey, you have access to this
1:56:57
course. I can refund it to you." Or it'll say, "Hey, you don't have access to this course. You haven't bought it. I cannot give you a refund." Okay, that is
1:57:04
our first multi- aent system at a high level. Hope this kind of makes sense. But what we'll do is we're now going to
1:57:10
dive into the code so you can see how each one of these agents is actually interfacing with state, making changes
1:57:17
to state, and you're going to see some more prompt engineering to get all of these different agents working properly,
1:57:23
specifically when it comes to using tools to manage state. So, let's hop in so you can see all of this in action
1:57:28
inside of our code. All right, so now it's time for us to dive into the code portion of our multi- aent system. And
1:57:34
what we're going to do in this second part is walk through everything step by step because I want to make this as easy
1:57:40
as follow as possible. So first things first, we're going to look at our main.py because this is where we have all of our core logic for creating our
1:57:47
sessions, creating our runner and then actually handling user queries. And once we understand quick recap of all of
1:57:53
that, we're going to dive into looking at the core agents that are running everything inside of our application.
1:57:59
So, we're going to look at our root agent and we're going to look at all the sub aents with their prompts and tools so you can understand how everything is
1:58:05
working together when it comes to answering user queries, updating state so that you can master multi- aent
1:58:11
systems. So, we're going to speed through the main.py because a lot of this is just a recap from what you've seen before and we're going to focus
1:58:17
most of our time inside of these sub aents. So first things first is we are going to create an in-memory session
1:58:23
service like we've done to where we're going to save state just locally on our computer just for testing purposes.
1:58:29
We're going to create our initial state where we're going to say hey you are working with user Brandon Hancock. He
1:58:35
hasn't purchased any courses yet and he hasn't made any conversations yet. We're just starting from scratch. From there
1:58:41
we are going to create a new session where we're going to say you are a part of the app name customer support and
1:58:48
this conversation you're working on belongs to user ID AI with Brandon and we're going to pass in the initial
1:58:54
state. From there we are going to create our runner like we've done multiple times in the past where we pass in two
1:59:00
raw ingredients the agent and then the session service. And then once we have
1:59:06
our runner created, we're now ready to start interacting with our users. And this is just a simple everything from
1:59:13
this part onward is basically us allowing our users to type in a request to us, us capture that request, and then
1:59:20
send it to our runner. That's pretty much everything that's happening here. And outside of that, there's just a bunch of logs. So most of the code
1:59:26
you're seeing after this point is just adding a ton of logs to show off to our final users of what's actually happening
1:59:32
inside the application. So long story short, we're saying great, give me your input. I will take in that input and I
1:59:40
will pass it over to the agent. Once I pass it over to the agent, what I'm
1:59:45
trying to do is just most of this is logs. So most of this is not necessary. I just wanted to make it super easy for
1:59:50
you to see everything that's happening once we start to run the code. But the most important part is right here where
1:59:56
we're going to go, okay, great. I now have the new message you gave me and I'm going to basically call run async where
2:00:04
run async goes all right I now have the user I know the session and the new
2:00:09
message I'm going to pass everything over to the agent so that it can understand what response it needs to
2:00:14
generate who the agent needs to delegate work to in order to give us a proper response from there we're going to
2:00:20
process the agent response which is mostly once again just logging statements where we're going okay great
2:00:26
I know what the agent agent said and I like I said 99% of this is just log
2:00:32
statements because most of the actual work is already being handled when you called run async. So we're just trying
2:00:37
to like hey is this the final response? Great. I will happily log everything so it's easy to view. So I'm going to skip
2:00:45
through most of this because most of it you've already seen in the past. So let's actually dive over to looking at
2:00:50
our core agent which is in the root folder of our customer service folder. And you can see we have a root customer
2:00:57
service agent. So let's walk through what's going on in this agent and how it's delegating work to its sub agent.
2:01:02
So at a high level we're need to give it a description so it understands what this agent does. And basically it's just
2:01:08
the root customer service agent for the community I'm building. And from there what you can see is it has core
2:01:14
instructions. And most of the questions that this is supposed to help with is to help the user with any questions and
2:01:22
then always direct them over to the specialized agent who can handle this response. So the core things that you
2:01:28
should be doing are you know understanding what the user asks and then route them to this appropriate
2:01:34
user. And to help the root agent better understand what the current state of the
2:01:39
application is is we are going to pass in the three different state values that
2:01:45
we have where we're going to say hey the username is username. Here's all the
2:01:50
courses they've purchased so far and outside of that here are all the core events that have happened when working
2:01:57
with this agent. Now, now that you have access to all that information, here's how you can access and pass along over
2:02:04
to the appropriate agents that you have access to. So, first things first, you have access to the policy agent. And
2:02:10
here's what the policy agent is good for. Mostly just answering questions about customer support, course policy,
2:02:16
and refunds. The sales agent is for answering any questions about making purchases. And you can see the current
2:02:23
price of it. Finally, if someone has a question about a specific topic within a
2:02:29
course, you're going to send them to the course support agent. And you can only do this if the user has purchased the
2:02:35
course. And what's great is because up top, we've already told the agent what
2:02:40
courses the person has purchased. It's obviously going to know, oh yeah, I can't even direct a user over to this
2:02:46
agent if they haven't purchased a course. And then finally, what we're going to do is if anyone has any
2:02:51
questions about purchase history or refunds, we'll send them over to the order agent. So, as you can see, most of
2:02:56
the instructions at the root level are all about delegation and briefly explaining what all the underlying
2:03:02
agents do and when we should call on them. So, it's a lot of instruction giving. From there, the core part that
2:03:08
you'll notice is we've just given it access to the four sub agents that it has access to. So, let's dive through
2:03:13
each one of these one at a time. So, first things first, we're going to look at the policy agent. And think of this one as almost like a rag agent to where
2:03:20
it's basically just like, "Hey, you have a question? Cool. I'll look at the policies we have and generate an answer." So, you can see it's just a ton
2:03:27
of policy questions of like, "No self-promotion, here's the behavior you need to have, here's some policy on
2:03:33
refunds, here are access to, you know, course access." It's basically just a bunch of like general Q&A questions. So,
2:03:40
this is super helpful. definitely recommend you stealing inspiration for this as you go off and build your own real world agents. Now, let's go look at
2:03:46
the sales agent because this is where things start to get fun where we begin to allow agents to update state and
2:03:52
start to purchase courses. So, the sales agent, you know, hey, you are a sales agent. Here is all the current
2:03:59
information about the current user. And here is the course that you are trying to sell. It is a full stack AI marketing
2:04:05
course. It's $150. Here's what's included in the course. And here's what the user will learn when interacting with the user.
2:04:13
You know, please check to see if they already own the course. If they do own it, remind them they have access to it.
2:04:19
If they don't have access to the course, just briefly explain the value proposition of the course and ask them
2:04:25
if they want to purchase it. Then after they have purchased the course, what you'll do is track the interaction. So
2:04:32
we'll update event history and then basically be ready to hand off the course to support because once they
2:04:37
purchase the course we need to be able to answer questions about it. So that's this at a high level. And if the user does want to purchase a course here is
2:04:44
what will happen. So first things first is we have to pass in tool context because in order for our tool to update
2:04:51
state we need to pass in tool context. And what we can do is first look at to
2:04:57
see all right what inside of state what courses has this user purchased and we
2:05:04
need to pass in a default value. So in case for whatever reason this value in state is blank. You always want to have
2:05:09
a fallback value. So this could if if we were working with something else this could be a blank like no courses but in
2:05:16
our case we're we're storing all of our courses in a list. So that's why we're putting it in a list. From there, what we're doing is some simple Python logic
2:05:23
to say, okay, I would like to iterate through all of the different courses that the user has purchased to check to
2:05:30
see if the course ID basically I'm just trying to get all the course IDs. And then from there, what I'm trying to
2:05:36
check to see is like, okay, has the user purchased this course ID? So, we're saying if this course ID is in the list
2:05:44
of course IDs we have, what we're going to do is say, hey, you already own this course. You can't buy it again. So
2:05:50
that's what that logic says. Then what we're trying to do next is we're going to go great. So we've made it this far.
2:05:56
We know they don't have access to the course. So now what we're going to do is purchase the course. So what we're going
2:06:01
to do is we're making a new list where we're going to iterate through all their existing courses and continually add the
2:06:08
existing courses to the list. And then finally, what we're going to do is add the new course we've just purchased for
2:06:14
them to the list. And then once we have the new state up and ready, we're going
2:06:19
to save it to the state that's shared amongst all the agents. So quick recap, what we're doing in this logic right
2:06:26
here is saying, great, I'm updating your list of courses you own with a new one.
2:06:32
And once we have the proper updated list of all the courses you've bought, we're then going to save the updated list to
2:06:40
state. That's all we're doing right here. And we're also going to update your interaction history to say, hey,
2:06:46
you purchased this course at this timestamp so that we have a history of
2:06:51
all key events when working with this agent and specifically so that when other agents are looking at what's
2:06:57
happened so far, they can easily look at the interaction history. All right. Finally, from there, we are going to
2:07:02
follow tool best practices where we are going to update and return state. So
2:07:08
state instead of just saying, "Hey, true, we purchased it." No, we follow best practices where we give status, we
2:07:14
give a message, and we properly say, "Here's what you bought in at this time stamp." So that was a little bit of a
2:07:19
deep dive, but hopefully you got to see a lot of the core principles of how we're passing in state dynamically, how we are following best practices and
2:07:27
allowing our tools to access state through tool context, and how we are
2:07:32
reading from state. And then from there, you're seeing how we are saving back to
2:07:38
state. So you're seeing, you know, you're becoming a master of all the core components of working with multi- aent
2:07:43
systems and following best practices with tool calls. Okay, we are almost done reviewing this. So let's look at
2:07:49
the core support agent and we'll speed through these cuz the rest of these are pretty much just instruction heavy. So
2:07:54
at this point, per usual, we're passing in state into this agent so it knows exactly what's going on. And then based
2:08:01
on what courses the person has purchased, we then can answer questions
2:08:07
appropriately. So if the user owns the course, great. What we'll do is help
2:08:12
them with the course. Cuz if they own it, we can answer questions about it. If they don't own the course, we're going to direct them over to the sales agent.
2:08:18
So the sales agent can say, "Hey, you don't own this, but it looks like you're interested in it. I'd be happy to answer questions. you just got to buy it first.
2:08:25
So then what I do is then just give a ton of information about the course. So I say, "Hey, in section one, here's what
2:08:30
you learn. In section two, here's what you learn." And I just keep going throughout the rest of the course so that there's some highle overview of
2:08:37
what's being included in the course. Finally, the last agent is the order agent. And the whole purpose of the
2:08:43
order agent is to allow persons to ask questions about the purchase history and process refunds. So what we're doing is
2:08:50
giving all the state per usual. Hopefully, you're starting to see the core principles seeing used over and
2:08:55
over and over again. And then what we're trying to do here is just say, "Hey, if they ask about the purchases, just let them know what they've purchased. If
2:09:02
they want to refund, what you need to do, verify that they own it, and then from there, if they do own it, give them
2:09:08
a refund if it's been under 30 days. So, yeah, that's pretty much all we're doing inside of our agents. And if they do get
2:09:16
a refund and things go through successfully, what we're trying to do, per usual, the exact same thing what we
2:09:21
did with the order call a second ago, the order tool call, but now we're just undoing it. So undoing it follows the
2:09:27
exact same process at a high level. You get state, you check just to confirm to make sure they own it. If they do own
2:09:34
it, what we're going to do is remove the course from the list. Once we've removed the course from the purchased course
2:09:42
list, we're going to update state. We're going to update our interaction history to say great, it looks like we did get a
2:09:50
refund. So that's what we're updating our interaction history with, saying they refunded the course at this time.
2:09:55
And we're saving it back to state. And then we're returning the tool call to say, yep, this was a success. They
2:10:01
refunded the course and here's some additional information. Okay, so you now got to see all the core parts of this in
2:10:07
action. So what we're going to do is now that you've gone through and seen everything, understand part by part from
2:10:13
prompts to tool calls to tools updating state. So what we're going to see now is we're going to go off and run this so
2:10:19
you can see exactly how all of these works together. So let's kick everything off and start running the demo. All
2:10:25
right, so now let's dive into the fun stuff where we're going to run our agents. And as a quick reminder, you need to be in folder number eight so you
2:10:32
can run this example and you need to have your virtual environment activated. Once you've done both of those, we can
2:10:37
run everything. So, type in Python main.py and this will create your session. It'll get everything set up and
2:10:43
ready to run. So, we can now say, "Hey, what courses do you have for sale?" Now,
2:10:50
what this will do is spit out a ton of logs so you can see everything that's happening. So, you can see we always have a before state and an after state
2:10:57
so you can see exactly what's happening. And right here in the blue in the middle, you can see the agent response.
2:11:04
So you can see it goes okay great I have a course available it's priced at this amount of money and you can see that the
2:11:10
customer service agent gave us this response so we can say yes I would like to purchase that
2:11:17
purchase that course from there what will happen is we will be sent over to the sales agent who's responsible for
2:11:24
closing the sale and we goes great I can help with that here's the course it's a sixe program the price is this would you
2:11:29
like to proceed with the purchase yes please purchase the course. From there, what will happen
2:11:37
is you can start to see we make some state changes. So, before saying I'd like to buy the course, we didn't have
2:11:43
access to it. Afterwards, though, you can see the agent said, great, you successfully bought it. You're enrolled.
2:11:48
Would you like to start learning? And you can see that our state after running this request now has the course. So,
2:11:54
awesome. We now have our agents managing our state through tools. Really cool. So
2:12:00
now we can say yes, what are all the modules inside of the program? From
2:12:06
there, what will happen is we should be directed over to the course support agent. Yep. Course support agent. And
2:12:13
the agent will say, "Okay, yep. Because you have access to all of the because you've purchased this course, I can give
2:12:19
you answers now. You bought it on this date and here are all the different modules. Do you have any questions about anything in particular?" And we could
2:12:26
dive in. But in our case, we're going to say, "No, I'm good. I don't want the
2:12:32
course any more. Give me a full refund." And what this should do is move us over
2:12:39
to our support agent. So, what you can see here is our before state shows that
2:12:45
we have access to the course. Then, we should get delegated over to the proper
2:12:50
agent. In our case, it's going to be the order agent. and it'll go great I have refunded your course completely the
2:12:58
money will be sent back to your account in three to five days and you've been remove the course has been removed from your account and what's awesome is you
2:13:04
can now see our course has been removed from state so our order agent properly removed the course so yeah so this was a
2:13:10
quick overview guys of showing you how multi- aent systems can work together and they can be more intelligent by
2:13:16
sharing state because when they share state they can know exactly what you have access to don't have access to and
2:13:21
respond appropriately so hopefully You guys found this example super helpful and now it's time for us to move over to
2:13:26
example number nine where we're going to dive into callbacks so you can learn how we can manage all sorts of interactions
2:13:33
between agents and LLN and have full control over our agent workflows. So let's hop over to example number nine.
2:13:38
Hey guys and welcome to example number nine where you're going to learn about the six different types of callbacks that you can add to your agent workflows
Example 9: Callbacks
2:13:45
to help you control every part of your agentic systems. And there are six different types of callbacks that we're
2:13:51
going to cover here throughout this example. So the before and after agent call back, the before and after model
2:13:58
call back, and the before and after tool call back. So what we're going to do in this example is first head over to the
2:14:04
doc so you can see what each one of these different types of callbacks do and some of the best practices. And then
2:14:09
from there, we're going to quickly cover each of these different examples I prepared for you guys and run them. So this one's going to be a little bit more
2:14:15
interactive than the other examples. So let's go ahead and hop over to the docs. you can understand everything you need to know about callbacks. All right, so
2:14:21
the first thing I want to show you guys is this highle overview of when each of the callbacks gets triggered inside of
2:14:27
ADK. So the first two callbacks that you're going to see in use are going to be the before and after agent call back.
2:14:34
These are going to be before any logic happens inside of your AI solution. So this is right when things get kicked
2:14:41
off. What do you want to do? And then once everything is done being processed with your agent, what do you want to do
2:14:47
with the information that you now have? So that's the before and after callback. And you're going to see some more examples of these in just a minute. The
2:14:53
next callbacks I want to show you are the model callbacks. So the before and after model callbacks are going to be
2:15:00
used before you pass information over to Gemini or OpenAI or Claude. What do you
2:15:05
want to do with the request you're sending over to these models? So you can do a little bit of pre-processing and adding some information and you can do
2:15:12
some like validation or some checking afterwards. Then finally we have before and after tool call backs because our
2:15:19
agent has the ability to call tools such as get the weather, get the stocks and sometimes what you can do with these is
2:15:25
maybe add in some validation and add in some additional information and then once you get back results from the tool,
2:15:32
you can process it to make sure it included the proper information. So, these are the six different callbacks we're going to be diving into. So, let's
2:15:38
head over to the doc so you can see some of the core principles that ADK tells us
2:15:44
when and why we should use each one of these callbacks. All right, so I've zoomed everything in so we can easily walk through the six different callbacks
2:15:51
and cover when and why you would want to use these callbacks. So, to start off, let's look at the before agent call
2:15:57
back. And this is the one I use the most and you'll most likely use the most as well as you work with ADK. And you know,
2:16:04
you saw the before agent call back is triggered before anything gets called inside of our agentic system. And the
2:16:12
main reason you'll want to use this different callback is to set up resources and state before the agent
2:16:20
runs. So this is where I like to do some state hydration, which is just a fancy
2:16:25
word to say, hey, before this agent runs, let's go fetch some information about the user. So let's grab their
2:16:30
current order history. Let's go grab whatever subscription they have and let's just give all that information to
2:16:37
the agent so when it's running it has everything it needs to know. So main reason to use this one is for setup.
2:16:42
State setup is when I like to use this one. Okay. Now the next one you're going
2:16:48
to be using is the after agent callback. And this one runs after everything is
2:16:53
done. So you've you've made all the requests to the LLM, you've done all the tool calls, the agent's done running.
2:17:00
then the agent call back is triggered. Now when and why would you want to use this one? So their main options are for
2:17:08
postexecution validation and logging. Those are the main ones I like to use. So after the agent's done running, you
2:17:14
can just make some logs to if you have this application running in production, you can just make some additional logs
2:17:19
of like, hey, I gave the user this information. So you can just really just save it. That's the main one I like to
2:17:25
use it for. And if you want to modify any state, so if you want to keep up with the number of requests the user has
2:17:32
made, this is a great place to modify state afterwards. Okay, the next one we're going to look at is the before
2:17:38
model call back. Now the before model call back, just remember this is before we trigger OpenAI, Gemini, Claude,
2:17:46
whatever model we're working with, we trigger this before we send the request over to the large language model. Now,
2:17:53
when and why do we want to use this? Well, a few different examples that ADK
2:17:58
recommends is for adding additional dynamic instructions or injecting some
2:18:03
examples based on state or model configurations. Now, I don't really use this one that much, but what you could
2:18:09
do is also add in some guard rails. And you'll see this in an example that we're going to work on together, but you can
2:18:15
use Python to review the request we're sending over to the large language model to say like, hey, are they using any
2:18:21
profanity or are they doing anything that's, you know, they shouldn't be asking inside of our agent? And you can
2:18:26
just do a quick check to say, oh, they are. Okay, I'm not going to allow the user to send this request to the large
2:18:32
language model. This is not allowed. So that's what we're going to be working on together. And you're going to see later
2:18:37
in a second how you can, you know, quit the the loop if the user tries to ask
2:18:43
for something that they're not allowed to. So you can either yeah skip it basically. So you're going to see that in a second. Then the next one you can
2:18:49
see is after model call back. So once Gemini or OpenAI gives us an answer,
2:18:55
what we can do is alter the information given back to us. So that's one of the
2:19:00
main reasons I like to use the aftermodel callback. it is to reformat the response. So if there's any certain
2:19:06
words you don't want the agent to use, you can actually replace keywords. You can log anything you want or you can
2:19:13
censor or blur out information. So for example, if the agent returned something it wasn't supposed to, like maybe the
2:19:19
user's ID or anything like that, you could actually blur it out so the user can't see it. All right, the next two
2:19:26
that we're going to look at are going to be tool execution callback methods, specifically the before and after. So
2:19:32
the before tool callback, it does exactly what it it says. It gets triggered before the tool gets called.
2:19:37
And the main reason I like to use this one are to basically inspect and modify the tool arguments or perform
2:19:45
authorization. So, for example, if the user was going to make a request to,
2:19:50
let's say, add an additional item or purchase it, we could make sure that the user ID that was making the request
2:19:57
actually matches the account that we're working with to make sure nothing weird's happening or they're not trying to trick the LLM to make a tool call
2:20:03
they weren't supposed to. So, this is when it comes down to authorization checks. So, the other one that we can
2:20:09
start to work on is the after tool call back. And the reason most of the time people use this one is to really just
2:20:15
inspect, modify, and log the tour results. So those are the main reasons people use this one. So, but this one,
2:20:22
like I said, yeah, this one's not the craziest. Or you could save information to state. So these are all the six
2:20:28
different types of callbacks that you can use highle purposes. But now what I want to do is dive into the three
2:20:34
different examples I've set up for you guys so you can see each one of these callbacks in action at a high level and
2:20:41
understand how you can use them in your code. So let's hop over to our cursor and start seeing these callbacks in
2:20:47
action. All right, so now it's time to get our hands dirty and dive into some code. And we're going to walk through each type of callbacks one at a time.
2:20:54
So, we're going to look at the code, run it so you can see everything in action, and we're going to iterate for each of the different types before the agent
2:21:01
ones, the model ones, and the tool ones. Let's go ahead and dive in to our before and after agent callbacks. So, we're
2:21:07
going to open up our agent.py file for this quick example. So, you can see the before and after agent callbacks in
2:21:13
action. So, in order to add callbacks to your agents, what you can do is update
2:21:20
the before and after agent callback. like they make this so clear when it comes to naming. And what you want to do
2:21:25
is for each one of these callbacks, you want to point to a function. Now, there's a few core things you need to
2:21:31
know about these functions before you start to work with them. So, the first thing is you need in order for callbacks
2:21:37
to work appropriately is you need to pass in the callback context. This is what's going to allow the agent to
2:21:43
access state and all the other necessary information it needs to properly handle what's going on. From there, you want to
2:21:49
make sure the return type is optional and returning content. Now, what why why are we doing this? Well, you'll see in
2:21:55
just a second. If you want the agent to continue as normal, you return none. So,
2:22:01
that's why it's optional because we're going to return none if everything's okay. If for whatever reason the user did something we didn't like, we would
2:22:08
return a message saying, "Hey, I'm skipping this because of whatever reason." So, you return none if things
2:22:14
go good. you return messages if you want to skip what's happening. So that's uh something that was a little weird to me
2:22:20
when I saw this for the first time. But let's dive into this before and after agent call back so you can see exactly
2:22:25
what we can do with these different callbacks. So if you remember what we want to do with the main reason we want
2:22:31
to use before agent callbacks is to log and to hydrate state. So what you can
2:22:36
see is we're taking in the callback context and the first thing we're doing is we are grabbing state with state.
2:22:43
What we're doing is just to test out some initial information is we are going to say all right state do you have agent
2:22:50
name as a key if not I'm going to update state to include the name and then from there what we're going to do is we're
2:22:56
going to keep track of our request counter so you can see hey does request counter exist in state if not this is
2:23:03
obviously our first request otherwise we're going to increase the state request counter outside of that we're
2:23:08
going to add a third key to state where we're going to keep track of the request
2:23:13
start time because in the after callback agent we're going to see okay well you started at this time and then you
2:23:20
finished at this time great I know it took about 10 seconds 2 seconds 1 second to generate this entire response outside
2:23:27
of that we're just going to do some logging so we can see and keep track of things as we run it awesome from there
2:23:33
you can see we have an after agent call back who accesses the same call back state and we're doing pretty much the
2:23:39
exact same thing so now we're going to grab state Now, we're going to get the current time. And then from there, we're
2:23:45
going to look at, okay, we're going to grab the start time, and we're going to subtract the current time from the
2:23:52
current time from the start time. And this is how we get, oh, it took you 2 seconds to run this entire request. And
2:23:58
we're just going to log this all out. So, enough talking about this at a high level. Let's go ahead and run this root
2:24:04
agent so you can see it in action. So, let's clear things out. Let's make sure we are in example number nine. And if
2:24:11
you look in example number nine, there are multiple folders and we want to go to the before and after agent. So cd
2:24:18
before after agent. Great. Once we're here, we can now run everything. So we're going to type in adk web. And this
2:24:24
will trigger out the, you know, the web interface that you're used to. And we'll open it up. And what we can do here,
2:24:32
let's get everything running. So select an agent. I think I did something wrong.
2:24:37
One second. So I made a quick mistake. We should not have cded all the way into these agents. We should just run the
2:24:43
program from the highle folder. So what you need to do is just run adk web here.
2:24:48
And this will get everything kicked off and going properly. So now you can see it gives you the ability to select an
2:24:54
agent. And we're going to run the before and after agent. So what we can do is say
2:24:59
hey how are you doing? And this is just going to showcase a few of the core components that we have. So hey I'm
2:25:07
doing well. From there, we can say it's doing well. And then if we dive into state, you can see it saved all the
2:25:13
important information that we asked it to do when it came to running an agent. And we can say, what is your name? And
2:25:20
what we would expect this to do is to update the request counter and the the start time. And if we close out of this
2:25:26
session and hop back to our logs, you can see because we had a bunch of logs, you can see, oh, the second request took
2:25:33
60 seconds. And I can see if I go even further up uh to call back number one,
2:25:39
you can see the first request took almost 2 seconds. So you can see that it's working and it's properly logging
2:25:45
everything that we showed. So now what we're going to do is quit everything and we are going to move over to the next
2:25:51
callbacks which are before and after model. Okay, so now it's time for us to look at the before and after model
2:25:57
callback example. So this is the agent.py inside of this folder right here. So, what we're trying to do inside
2:26:04
of this agent is showcase how you can filter content. So, someone gives you a request that you don't want, you can
2:26:10
quit and say, "Hey, that was a bad request." And we're going to log everything. Now, before we dive into looking at these two different
2:26:16
callbacks, I want to show you guys how easy it is to add them into your your agents. So, instead of doing the before
2:26:23
and after agent callback, we now just say before and after model call back. As
2:26:28
simple as that. And per usual, we just pass in the callback function we want to trigger. Now, here's what's different in
2:26:35
these new callbacks. Instead of only providing the callback context, you also
2:26:40
need to provide the LM request where the LLM request is going to include the message that we are trying to send over
2:26:47
to Gemini or OpenAI. So, what you can see is we can do exactly what we did
2:26:52
last time. we can pull out the state, grab our agent name, and then from there, what we're going to do is extract
2:26:59
the user's last message. And the reason why we're trying to do that is we want to iterate through all the message
2:27:06
content that was sent to us and we're reversing the list so we can get the newest item that's from the user. And
2:27:12
once we have that latest message from the user, we're going to save it here. Then what we're going to do is showcase
2:27:19
that. We're going to say if we have that user message, what we want to do is just
2:27:24
showcase it. Then from there, what we're going to do is say, all right, does that
2:27:30
latest user message include a bad word? So, we're going to say, hey, does it include the word sucks? If so, what
2:27:36
we're going to do is throw a bunch of logs saying, hey, inappropriate content was detected. And this is where we can
2:27:43
start to alter the life cycle of our agents and our LLMs. So instead of
2:27:49
returning none, we're going to return an LLM response. And this LLM response is
2:27:54
going to go, hey, you tried to make a request and we're going to say, hey, I
2:28:00
cannot return like we're going to basically instead of the LLM responding, we're going to respond for it. So we're
2:28:05
going to say, hey, this model, we're going to say, I cannot respond to this message because it includes inappropriate language. Please rephrase
2:28:12
your request without words like this. Now, that was only if the message included a bad word. If it did not
2:28:19
include a bad word, what we're going to do is just return none because returning with none just continues with the normal
2:28:26
life cycle. Then finally, what we're going to do is with the other option, which is the after model callback, all
2:28:33
we're going to do is do some simple replacements. So, if the LLM responded
2:28:39
with something, we can actually change the response. So, I'm going to scroll down just so you guys can see it. So, if
2:28:45
for whatever reason the LLM responded with an empty response, we're just going to skip it. Otherwise, if the LLM does
2:28:50
include some text, we're going to say, okay, what I would like to do is iterate
2:28:56
through all the words you said. And if you included a word like problem or
2:29:01
difficult, I want to change the word with challenge or complex. And then what
2:29:06
you can do is you go through the original you go through the original response that they gave us and we're
2:29:12
going to save it to modified text. So a new variable and we're going to iterate through each one of the words that we
2:29:19
want to replace. And we're going to replace them inside of our text. And we
2:29:24
are going to return if if any of the words included in our case problem or
2:29:29
difficult we are going to replace them. And we are going to return our modified
2:29:35
answer. So if we replace something, we're going to say modified true. And so if we modified, we're going to say,
2:29:40
"Hey, I definitely did change something, and I'm now going to return that LLM
2:29:46
response." That's all we're doing. If it did not include a word we were trying to replace, we're going to return none. So
2:29:52
that's all we're doing inside here. And inside the readme, I actually have a few different examples that you can test
2:29:58
things out with. So let's see. Down here, I have some examples that you can run. Let me show you guys really
2:30:05
quickly. Yeah. So to test model callbacks, you can say this website sucks. Can you help me fix it? So let's
2:30:11
go run everything so you can see these in action. So let's run it again. So we're going to do ADK web. This will
2:30:18
trigger our website to spin up. Now we can go to the before and after model session and we can type in this message.
2:30:25
This website sucks. Can you help me fix it? And now the model's instantly going to say, "Hey, I cannot respond to
2:30:31
messages when using words like suck." So this is pretty much just exactly what we
2:30:36
told it to do. So if you were to hop back over to our code, you can see this is the exact message we said to do right
2:30:43
here. I cannot use respond with messages like that. Okay, cool. So now let's try out the other one. So we can say, what's
2:30:49
the biggest problem with machine learning today? So we can now try this example. So, we're going to open it up
2:30:55
and we would expect it to replace the word like we told it to. We would expect it to replace phrases like problem with
2:31:02
challenge. So, let's open everything up. And now inside the before and after model call back, if I was to send this
2:31:09
request in, instead of it saying challenge, it will get replaced. And I believe we can. Yeah. So, we can dig in
2:31:17
to the response. So, one of the biggest So, this is what the model responded to. It responded with one of the biggest
2:31:23
challenges or one of the biggest problems with machine learning is that it's data bias. But what you'll notice
2:31:29
is the LLM responded with the word problem, but because we updated the model after callback, we said, "Hey, use
2:31:36
the word challenge here." So you can see it is it's working in real time. So this is a cool way if you want to like make sure you speak always in a certain way,
2:31:43
you can alter the response or filter out something. If they give you an API key or something that you shouldn't show back to the user, you can always filter
2:31:49
it out. Okay, cool. So you now got to see before and after model call backs in action. So now what we can do is go over
2:31:56
to the final call back which is the tool before and after callbacks. So let's hop over there so you can see this one in
2:32:02
action. Okay, so it's time for us to look at our final example which is going to be the before and after tool
2:32:08
callbacks. And for this example, we are building an agent that looks up the capital cities of different countries.
2:32:14
And because we're working with the before and after tool callback, well, we obviously need to have a tool that we're
2:32:21
trying to alter the functionality of for these before and after capabilities. So, what I'd like to do is first just show
2:32:27
you the tool we're trying to use and then we're going to walk through what we're trying to alter in these callbacks. Okay. So, what tool are we
2:32:33
trying to use? Well, we're creating a tool that takes in a country and once it takes in a country, it looks up to see
2:32:40
does that country exist in here? And if so, I'm going to return the capital city. So yeah, that's what the tool is
2:32:46
trying to do at a high level. Super straightforward. But now let's first dive into the before tool call back so
2:32:52
you can see it in action. So the before tool call back has a few key parameters you have to pass in. The first is the
2:32:59
tool. What tool are we trying to use? From there, we need to know what arguments we're passing into that tool.
2:33:05
And then finally, the tool context. So this is how we access state like in all the previous examples. So in this
2:33:11
example, we're trying to do two different things. First, if the user gives us uses the tool get capital city
2:33:19
and they pass in an argument such as America, we want to alter that argument
2:33:25
to say United States. So we're basically correcting the arguments that a user passes to us. And we're going to return
2:33:32
none because return none just means proceed as you normally would. But the kick is we have altered an argument
2:33:38
passed in. Another option is if the user calls get capital city tool and the
2:33:44
country they pass in is restricted. What I want to do is alter this tool call to
2:33:51
return this result. So we're not going to call the tool. We're canceling the tool call before it happens and just
2:33:56
returning this result. So that's exactly what we're trying to do with the before tool call back. So what we can do is run
2:34:03
this so we can see it in action. So let's get everything ready. So we are going to do ADK web and we are going to
2:34:10
open up our before and after tool and we can say what is the capital of America
2:34:18
and what it'll do is it will get the capital city and it will return the capital city and it'll say oh it was
2:34:25
Washington DC. Now if you look here what happened though is we actually made some
2:34:31
changes and you can't see the changes inside ADK web. you have to hop back to our terminal and inside of our terminal
2:34:38
we had some raw logs set. So you can see the user passed in what's the capital
2:34:44
city of America but then before the tool got called right here. So function call
2:34:49
you can see we updated the arguments to now say United States and because normally it would have just passed in
2:34:56
America but we altered it to pass in United States. So pretty cool that it
2:35:01
did that. Now let's go try the other example. So in our case, the other example we wanted to try was if they
2:35:07
asked about restricted. So let's open this up and we can say on our before and after tool call, what is the capital of
2:35:15
restricted? And in this case, it's going to return like, hey, I can't fulfill that request. You know, not valid.
2:35:21
Please return a valid country. But if we were to do a normal country, so like what is
2:35:27
the capital of let's just do France, this would work nor like normal like it
2:35:33
was supposed to do and it would go off and say, "Yep, the country is France. I'm calling this tool and then I got
2:35:40
back the answer which is Paris." So yeah, we have the before functionality working like a champ. So now let's
2:35:46
quickly review the after call toolback. So when it comes to the after tool call
2:35:52
back, this is where we can alter the tool response. That's the main functionality of altering the tool call
2:35:58
back. So what you can see is we're just doing a bunch of logs to say like, hey, what tool got called? What were the
2:36:03
initial arguments passed in? And what was the original response of the tool? Then from there, what we can do is make
2:36:11
some changes. Oh, and before we do that, I do just want to call out the properties. you do need to pass in the tool that's getting used, the arguments
2:36:17
that were passed to the tool and then tool context and tool response. These are the main ones. So the only one that
2:36:23
got added new was the tool response because obviously the tool generated a result. So we now have the opportunity
2:36:28
to alter it. So what we're going to do is we're going to say all right if the user basically passed in so if the tool
2:36:35
let me restate this if the tool get capital city was called and Washington DC was in the original result what we
2:36:43
want to do is alter that response to say okay I want the modified result that I'm
2:36:51
storing here to say okay the answer was Washington DC and then we're going to add this fancy little note at the end so
2:36:57
we have a nice little emoji So that's all we're doing. We're just long story short for all of this code right here is
2:37:03
we're just altering the original response that was given to us to include the original result and then add in some
2:37:09
additional text at the end. So let's try this out. So let's do we're going to run
2:37:14
it again and this time we're going to say what is the capital of USA. Let's go
2:37:19
ahead and open this up and we're going to select the before and after tool and we're going to say what is
2:37:25
the capital of USA? And now what it'll do is it will return the original result
2:37:32
which was just Washington DC but then it's adding that fancy note at the end that we told it to. So you've officially
2:37:38
altered the tool response using the after tool call back. Okay, you guys are
2:37:43
now officially pros when it comes to all six different types of callbacks that
2:37:48
you can use inside your agents. Super excited for you guys to wrap that one up because those are super helpful and
2:37:54
you're actually going to see us use the before agent call back. numerous times going forward because it's a super handy
2:38:00
one to use. So, now that we've knocked that out of the way, we're going to start diving over to our workflows,
2:38:05
which are going to include the sequential, parallel, and loop agents. So, let's hop over to example number 10
2:38:11
so we can start working on sequential workflows. Hey guys, and welcome to example number 10, where we're officially starting to work on our first
Example 10: Sequential Agents
2:38:18
type of workflow agent. And in this example, we're going to focus on the sequential workflow where agents work on
2:38:25
a task one after another. So what we're going to do in this example is first hop over to the docs, look exactly at what
2:38:32
ADK says about these workflow agents, and then we're going to look at this lead qualification pipeline example that
2:38:39
I've created for you guys where we have validator agents that then pass the results to a score agent which then
2:38:44
passes the result to a recommendation agent. And then in part two, we're going to look at this code that I've set up for you guys so you can see a working
2:38:50
example. And in part three, we're going to run it. So let's hop over to the doc so you can see everything in action. All right, so we're in the sequential agent
2:38:56
docs. So let's quickly cover what they are, how they work together, and when we should use them. Okay, so sequential
2:39:02
agents, basically it's a type of workflow agent, which means our agents are going to work in a particular
2:39:07
pattern. And in our case when working with sequential agents all the sub aents you provide to a rootle agent are going
2:39:14
to work in the order that you specify. So the most important thing to note is when you look at the code agents will
2:39:22
work in the order that you pass them in in the sub agent list. So if you have agent 1 2 3 it will always run agent
2:39:28
123. So execution occurs from first to last. Okay. So here's an example of why
2:39:33
you would want to use a sequential agent. Let's imagine you were building an agent that could summarize any web
2:39:38
page using two tools. It first wanted to get the page content and then summarize the page. Well, because you can't
2:39:45
summarize a page until you have the page content. This would make for a great use case to start using sequential agents
2:39:52
where first you would always get the page content and once we've grabbed the page content, we would then go over to
2:39:59
option agent number two where you would then summarize it. So that is a sequential agent in a nutshell. So
2:40:05
here's just a quick example of what it looks like inside a sequential agent. You'll see that you always provide sub
2:40:10
agents where this agent will always be triggered before this agent. And the important thing to note is that you are
2:40:17
not, you know, passing state like this arrow does not mean you're passing information from agent A to agent B. You
2:40:23
have to use shared state like we've been doing throughout the rest of these examples here together today. So if you
2:40:30
wanted agent two to have information that agent one generated, you would need to, you know, write that to state and
2:40:37
then sub agent 2 would pull that down. So that's super important to note. So what we can do is we're going to hop
2:40:43
over to the code example I've created for you guys, walk through it step by step so you can see how you can create these agents, share state between them,
2:40:50
and work together on building, you know, your multi- aent systems that work in a nice workflow. So let's hop over to the code. All right, so let's start to look
2:40:57
at how you can start to use sequential agents with inside of ADK. Thankfully, it's a super simple change. So, right
2:41:03
now we are inside of the lead qualification folder and we are in the lead qualification agent. And in order
2:41:10
to start working with sequential agents, all you need to do is import sequential
2:41:15
agent from here. Normally, what you would do is import agent. So, if you look at all of our other multi- aent
2:41:21
solutions, every time we're importing our regular agent, but this time instead of importing just a plain old agent,
2:41:28
we're saying, "All right, ADK, you are now working with a sequential agent." And inside of a sequential agent, I
2:41:34
first want you to, you know, trigger this this sub agent. So, the lead validator agent, the lead score agent,
2:41:40
and then the action recommener agent. So in this example, what we're trying to do is create a lead qualification pipeline
2:41:47
where I can give some information to this sequential agent and it will save
2:41:53
the result for me so I can figure out should I work with this customer or should I not. So what we're going to do
2:41:58
is first walk through each one of these agents at a high level so you can see what they do and understand how we're
2:42:03
saving the result of each of these agents so that the result from agent one
2:42:08
gets passed to agent two and the result from agent two gets passed to agent 3. So let's look at how we can do that. So
2:42:15
first things first, we are now looking at the lead validator agent and here's
2:42:20
all we have to do. We are going to give this lead validator some instructions saying, "Hey, you're here to validate
2:42:28
different clients that I give to you. So, I'm going to give you lead information and what this lead
2:42:34
information should include to verify that it's a complete qualification. Basically, to make sure that we're given
2:42:40
all the information we need, you're going to get their contact information, what they're interested in, what they
2:42:45
need, and some information about the company that they currently work for. If they're if they give us all the
2:42:50
information we need as a valid contact, we're going to say valid. Otherwise, you're going to return invalid. That's
2:42:56
all you need to do. And what we're going to do is save the result of this entire agent to the output key. So, if you
2:43:04
remember from way back when we were working on initially using agents to save the results to state, this is going
2:43:10
to save valid or invalid to this key inside of state. So, validation status
2:43:16
will either say valid or invalid. Okay, cool. So, now that we've understand what agent one can do, let's go look at the
2:43:22
lead score agent, which is going to score the lead that we are given to determine if they're a good fit for us.
2:43:28
So, we're going to say, okay, your job is to score. And what you need to do is look at the information that is given to
2:43:34
us and score the lead from 1 to 10. And I want you to score based off of how
2:43:40
urgent the problem is, if the person is a decision maker, if they have time and
2:43:45
budget. From there, what I want you to do is just give me back a numeric score and a one-s sentence justification of
2:43:52
why you think we should work with them. So, here's some example outputs. So, we could say eight, which is like, hey,
2:43:57
they're a good decision maker, clear budget, the great contact. Or three, we could say, hey, you know, they're not
2:44:03
really interested, no timeline, no budget, so they're not a great contact. And once again, we are going to save the
2:44:08
output of this to the lead score key so that the result like one of these will
2:44:14
be saved to state. Okay, great. So, we're all just building up towards working towards the final step in our
2:44:19
sequential workflow, which is all going to be inside the action recommener agent. Now, what this agent is going to
2:44:26
do is it is going to take in all the information that we've built so far from
2:44:31
our previous steps inside of our sequential workflow. So, we're going to pass in the keys right here. And if you
2:44:37
just notice the lead score key, this is exactly what is mentioned here. So lead
2:44:43
score key. This is exactly what we have in our recommener. So this is where those keys that we were saving, the key
2:44:49
values we were saving to state, this is where we're now getting access to them. So we can start to share state between our agents. And from there, we're going
2:44:56
to say, all right, using the information that I've just given you, I want you to create a recommendation on what next
2:45:03
steps we should take for this agent. So if the lead score is invalid, just say
2:45:09
what additional information we need. then based on the other types of score like if it's a bad score, a good score
2:45:16
or a great score suggest what we need to do next. So this is sequential workflow
2:45:21
in a nutshell. So what we can do now is we'll hop back to our root agent so we can kick everything off so you can see
2:45:28
it all in action. So what we're going to do is we're going to make sure that we are inside of our sequential agent
2:45:34
workflow. And I'm going to first open up in the readme I have some examples that
2:45:39
you can test here. So we'll first try an unqualified lead. So let's run this. So
2:45:45
ADK web and what we'll do is this will trigger our interactive session so we
2:45:50
can start chatting with it. So now we can pass in a lead. And if you notice to start there's nothing in state. But if I
2:45:57
pass in a lead for John Doe and he's a bad lead, we can watch what happens. So
2:46:03
agent one would trigger then agent two would trigger then agent three. So all
2:46:08
of these agents right here are getting wrapped up inside of a sequential workflow. So sequential workflow really
2:46:14
is nothing more than just a wrapper around all the three agents that you want to do all the work for you. And
2:46:20
what you would notice is as we were running the agent in real time, it was saving the results to state. So agent
2:46:27
one spit out the if it was valid or not. Agent two, the score was, you know, printing out the quality of the lead and
2:46:34
a justification of why they got that low score. And then the final agent, our third agent was saying, "Hey, based on
2:46:41
the two previous pieces of information, I recommend that John Doe is not a good
2:46:46
client for us to work with. I recommend just continue doing some education to see if he better understands what's
2:46:51
going on and if we can work with him." So, that's option one. But what we could do is let us hop back over to our
2:46:58
examples that we have set up. And in this time, we're going to pass in a qualified lead. So, let's scroll back up
2:47:05
to where things got kicked off a second ago. And now we can do another message
2:47:10
and this time do it for a great client. So, Sarah is a great client, great budget, leadership position, all around
2:47:17
great spot. So, you can see that's exactly what the agent said, too. This is the valid lead. This is a high score.
2:47:22
She's a CTO. She's trying to, you know, she has a budget and a timeline. And the recommendation is that Sarah's trying to
2:47:29
switch away from a competitor. What I recommend to do is schedule a demo with her and prepare a proposal. Yeah, you
2:47:34
can see it did exactly what it was supposed to do and it saved everything to state and that's how it was able to come up with this awesome response right
2:47:41
here. So yeah, that was sequential workflows in a nutshell. Hopefully that made sense because if you're familiar
2:47:47
with working with tools like Crew AI, this is probably more of what you're used to to where you have different
2:47:54
agents all working on one task. So definitely sequential workflows are amazing and we're now going to move on
2:48:01
to the next example where you're going to start to see how we can actually trigger multiple agents to go work in
2:48:07
parallel and then combine the answers. So let's hop over to example number 11. All right, welcome to example number 11
2:48:12
where you're going to start to work with parallel agents. Now in this example, we're first going to head over to the
Example 11: Parallel Agents
2:48:18
Google doc so you can see why they recommend to use these agents, when to use them. From there, I have a pretty
2:48:24
cool code example where we're going to monitor all of our computer analytics and, you know, use parallel agents to
2:48:30
quickly go off and find all the information about our computer and give us a nice little report. And then in the
2:48:35
third example, we're going to run this code that I've created for you guys. So, let's hop over to the docs so you can
2:48:40
see all the core information you need to know. Okay, so let's dive into what are parallel agents, when you should use
2:48:46
them, and then a quick example of how they all work. So first things first, a parallel agent, it's another type of
2:48:51
workflow agent where we are structuring our agents in a particular format to go off and do work. Now in the the case of
2:48:58
parallel agents, instead of agents, you know, being triggered one after another, which is usually slow because you have
2:49:04
to wait for agent one to finish, then agent two, then agent three. Well, with parallel agents, what we're doing instead is we are going to do things in
2:49:11
parallel. So where all of our agents are going to generate and do work all in parallel, so it's much faster. And then
2:49:18
afterwards once all the work's done is we can use all the information that they saved to state and then in the final
2:49:25
agent take all that raw information and spit out a nice report. That's the usual type of workflow for a parallel agent.
2:49:31
So whenever you want to focus on speed, this is the agent workflow for you, especially when you need a lot of work
2:49:37
to get done. So let's look at a few quick examples of what they recommend.
2:49:43
So in this case, if you wanted to do a parallel agent that you know, let's imagine you just wanted to do a lot of
2:49:49
work. Most basic example is just agent one does work, agent two does work, agent three does work, and they all
2:49:54
create outputs. Now, this is handy and helpful cuz you're going to get a lot done really quickly. But like I mentioned earlier, most of the time you
2:50:01
want to combine all of these results into something that the final agent can look at and generate a super nice report
2:50:08
that you can start to look at. That's usually what you want to do with parallel workflows. So now you've seen a high-level overview of what the agents
2:50:14
look like. Let's hop over to the code example where this will make so much sense cuz it's actually super easy to use. So let's hop over to the code so
2:50:20
you can see all this in action. Okay, so it's now officially time for us to get our hands dirty working with parallel
2:50:25
agents. Now in this example, we're actually using sequential agents and parallel agents. So don't let it confuse
2:50:31
you, but I'm going to walk you through everything step by step. Okay, so first off, what we need to do is look at our
2:50:38
root agent. And what I want to call out is our root agent has two sub agents. So
2:50:43
what's happening is the first agent is a parallel agent. This parallel agent, we
2:50:49
import it just like we do with everything else. Parallel agents up here, sequential agents, regular agents, we all import it from the same place.
2:50:55
Now, but here's what's happening under the hood. We are generating multiple agents to go off and do work. So the
2:51:01
first agent is going to be the CPU agent. So it's going to do work. We have a memory agent which goes off and looks
2:51:06
at how much memory we have available on our computer. And the final agent looks up how much hard drive space we have on our computer. And all of these agents
2:51:13
are going to get wrapped in a sequential workflow. That's exactly what the system information gatherer parallel agent is
2:51:20
doing. So when you see this right here in your head, you should be thinking, okay, I have three agents running in
2:51:26
parallel and they're just wrapped in one parallel agent. Great. Now going back to
2:51:32
our sequential agent, you can see the second item that we have is a system
2:51:37
report synthesizer. So what this is going to do is it's going to take all the information that these agents are
2:51:43
saving to state. So they're all saving to state and this system report generator is going to then say great I
2:51:49
understand everything that you've done. I'm going to put it in nice report. So the like final result is you're going to have just a quick repeat is you're going
2:51:55
to have parallel workflow that's going to have three agents and then you're going to have one final agent that's
2:52:01
going to work and all of this is going to live inside of this sequential agent right here. So sequential agent is
2:52:07
running the parallel agent first and it's going to pass their final results over to the system report synthesizer.
2:52:12
So hopefully that makes sense and hopefully you're starting to see like oh wow I can start to chain together parallel agents within sequential
2:52:18
agents. Like the world is your oyster. You can do whatever you want. So, what I'd like to do is first walk through what each one of these agents does at a
2:52:24
high level because I think it's pretty cool. And then you'll see how we start to save each one of the results from these to state and then access all the
2:52:31
saved information and make a nice report. So, let's dive into the CPU agent first. And when it comes to best
2:52:36
practices, what you'll start to know as you build larger and larger agent workflows is within each agent to keep
2:52:43
things nice and tidy, you'll first want to create your agent.py. And then if there's any particular tools that you
2:52:49
want this agent to use, you usually break them out into tools.py file to where eventually each folder is going to
2:52:55
have its own agent.py and its own tools.py. So it just keeps things very very clean and it keeps your files very
2:53:01
lightweight. So let's dive into looking at the CPU agent where basically what it's going to do is all it really is
2:53:08
going to do is call the get CPU data function and this is going to call the
2:53:14
psutils library. So, this is a library that we've already installed and what it's going to do is it's going to see
2:53:19
how many CPUs you have and it's going to put all this in a nice dictionary that we can return to our agent. So, you can
2:53:26
see this this is a huge bit of information we're going to return. So, we're going to turn the CPU stats, we're going to return all the cores, we're
2:53:34
going to return all sorts of information back to our agent. And the most important thing is let's get out of tools. All of that information that we
2:53:40
get from our tool call is going to get saved to CPU information. Great. So now let's go look at our next agent which is
2:53:46
going to be the memory info agent. Now our memory info agent once again is going to have instructions for like hey
2:53:52
your job is to go get anything related to memory when it comes to the computer and you're going to report back usage if
2:53:58
you know if they're using a ton of memory. And in our case we're going to have another tool once again going to
2:54:03
use the psutil library. And we're just trying to put as much information in this tool call as we possibly can and
2:54:10
return it in a dictionary because that's what ADK likes. It wants our tools to return dictionaries with as much
2:54:16
information as we possibly can for the agent to easily read through it. Per usual, we're going to save the results
2:54:21
to an output key so that it gets saved to state. And then finally, what we're going to do is go over to our disk
2:54:27
information agent. And what we're going to do with our disk information agent, pretty much same thing that you've seen for everything else. We're going to look
2:54:32
at what we have saved to our disk. If we have too much information saved to our disc, we're going to say, "Hey, it's
2:54:38
high usage." Then finally, we're once again calling the PS utils library where
2:54:43
we're going to check and basically make a few requests to see what disk we have available and how much we are using for
2:54:49
each device we have on our computer. So all in all, pretty cool code and we're going to return all the information. So
2:54:54
that's everything at a high level for all of our parallel agents that are going to go work separately because
2:55:00
there's no reason there's no reason for us to do agent one then wait a few minutes or a few seconds then call agent
2:55:07
two then call agent three afterwards like all of these can be done in parallel to save time. So that's why
2:55:13
we're doing this. And then finally, once all of these agents have gone off and saved everything to state, we're then
2:55:19
going to use the system report synthesizer to access all that saved information and make a nice report. So
2:55:25
this is where you can start to see how everything comes together. So you can say, great, you are here to generate a
2:55:30
nice report on my system. Here's all the raw information you need to know. You have access to CPU information that's
2:55:36
saved to state. You have access to memory and disk information that are also saved to state. and I want you to
2:55:42
make a well formatted report is basically in markdown that you can then show to me. So that's exactly what we're
2:55:48
doing. So let's run this bad boy so you guys can see it in action. So we need to go over to our example number 11 for
2:55:55
parallel agents. And now we can run ADK web. When we run ADK web, it's going to
2:56:01
kick off our server. And you can see it already shows us the root agent. And
2:56:06
just a quick reminder that root agent has a parallel workflow for the first agent and then the second agent is going
2:56:12
to be that system report. This is all handled under our a sequential agent that has a parallel agent and a regular
2:56:19
one. Okay, great. So what we can say is say please get the stats for my
2:56:24
computer. Now what this will do is it will trigger all sorts of states. So we should start to see each one of these
2:56:29
get triggered in parallel. I mean that happens so fast it's it's it's hard to keep up. See that's the power of parallel. But you can see at the same
2:56:35
time we made requests to each tool where normally if we were to not use parallel
2:56:41
workflows it would have been okay step one call get CPU great I got the answer
2:56:47
now I'll move on to the next one great I got the answer cool now I'll go to the third one got the answer so as you can
2:56:53
see this was so much faster from there in real time we were getting back all of the information in a nice little report
2:57:00
so each agent was spitting out the results so you can see when I click Click on this agent. You can see the
2:57:05
memory. Oh, this is pretty cool. I'll I'll zoom out so you guys can see it. So, you can see in our parallel workflow, we have access to three
2:57:12
different agents. And you can see when I click on each agent, like it just so happened that agent two finished before
2:57:17
agent one because in in parallel workflows, order is not guaranteed and it doesn't matter because it's all
2:57:22
happening in parallel. But you can see this agent was able to report back how much memory I have available, usage, and
2:57:28
so forth. The next I can see my CPU agent said, "Hey, your system has 10 cores. you're using not a ton. Great.
2:57:34
And then finally for my disc agent, you can see I have like external hard drives and everything hooked up. So everything
2:57:40
looks good. And then finally, when it comes to the final report, you can see uh cuz these were all wrapped in a
2:57:45
sequential workflow. So this one was step one and this one was step two. So you can see step two looked at all of
2:57:52
the state information. So I can actually scoot over here. So you can see in example number two, it was given access
2:57:58
to I can actually go in here and show you guys. Yeah. So your job is to be a system report information. And then
2:58:06
right here for CPU information, we actually passed in all the information from report number one. And then when it
2:58:12
comes to memory information, we passed in everything from report number two. So all this got passed in a prompt and then
2:58:18
it generated this super nice looking report for us. So we can get a good understanding of what's going on in our
2:58:23
computer and if we need to do anything else. And overall, thank god my computer's in good condition. I'd be hosed if it wasn't. I wouldn't be upset
2:58:30
if I got a new computer, though. And uh yeah, you can see everything is looking great. So this is parallel agents in
2:58:36
action. And just quick reminder, you want to use parallel agents whenever you want to do a lot of work at the same
2:58:42
time. All right, great. So now we are almost done, guys. We can now go to our final example, which is loop agents,
2:58:49
which is going to be one of the most powerful workflow tools available inside ADK. So let's hop over to our final
2:58:55
example, example number 12. All right, give yourself a pat on the back cuz you've officially made it to the final
Example 12: Loop Agents
2:59:00
example inside this ADK crash course. And in example number 12, we're going to
2:59:05
focus on adding in loop agents workflows to our toolkit. Now, what we're going to
2:59:11
focus on in this one is you're going to see how you can begin to use loop agents to have your agents iterate on a problem
2:59:17
over and over and over again to solve a specific problem until they get an answer. This is one of the most powerful
2:59:23
features in my opinion and it feels a lot like how crew AI in lane chain will
2:59:28
use agents in the react format which stands for reason and act where agents will continually think about a problem
2:59:34
and work on it over and over and over again until they get an answer. So this is a super powerful pattern and in this
2:59:40
example breakdown we're first going to head over to the docs look at what ADK recommends then we're going to dive into the code and then we're going to run
2:59:46
this bad boy. So let's hop over to the code so you can see everything you need to know. Okay, so when it comes to loop
2:59:52
agents, the main thing you need to know is loop agents are basically sequential
2:59:57
agents but on steroids. And what I mean by that is loop agents will continually
3:00:02
run until we've run out of iterations. So like, hey, only try to solve this
3:00:07
problem five times. So it'll run multiple times or until a specific condition is met. So we can say, "Hey,
3:00:13
please continue to search the internet until you find five resources that I can use for my report." So that's
3:00:20
continually solving the problem over and over and over again until we meet one of these criteria. A max iterations or
3:00:26
until we meet a specific condition that we specify. So here's a quick example of what ADK recommends. So let's say you
3:00:33
want to build an agent that can generate images of food, but sometimes when you generate a specific number of items, like five banana, it generates a
3:00:39
different number of those items in the image. So because you have two tools in your agent, you know, option one could
3:00:46
generate the image and then option or sorry agent two could count the food and basically you would have those agents
3:00:52
continue to go and work over and over and over again until it generated an
3:00:58
image that you know had the right quantity. So that's exactly what you would want to do when working with loop
3:01:03
agents. And they're actually super super easy to use, but there is a little bit of trickiness when it comes to exiting a
3:01:10
loop. So that's exactly what we're going to cover now in the code. So you can see all this in action. So let's hop over to the code. Okay. So it's now time to look
3:01:18
at our final code. So in this example, we are focusing on creating a loop
3:01:23
agent. And if you remember the core things to know about loop agents is that they exit when one of two things
3:01:30
happens. First, whenever we hit max iterations or whenever we meet a certain
3:01:36
condition that says we're good, we're done. We don't want to work anymore. And now it's time to quit. And you'll see
3:01:42
how we can do that in just a second inside of our sub agents. And the other thing, the core reminder to note is in
3:01:49
our sub agents, what happens is we always first do this one. We always do
3:01:54
the first one first and then we always go to the second and we just continue the cycle over and over and over and over again. So what we're also going to
3:02:01
do is inside of this agent is we actually have two parts to it. So part
3:02:06
one is we are going to create an initial LinkedIn post and then part two is going to be the loop where the loop is exactly
3:02:13
what you just saw where we have one agent that reviews it and then we have one agent that actually implements the
3:02:19
changes. So that's exactly what we have going on in here. So if we were to draw this out, step one is generate post and
3:02:26
then step two is we have our loop agents where our first agent is going to review
3:02:32
and the next one's going to refine and it's just going to go in a workflow just like this over and over and over again
3:02:39
until we get that beautiful LinkedIn post. So let's start to look at each one of these step by step so you can see how
3:02:45
state is shared amongst all of these different agents from our sequential agents all the way to our loop agents.
3:02:51
So let's hop into our initial post generator so you can see exactly what it's doing. So in this case we're saying
3:02:57
all right you are a LinkedIn post generator and what I would like you to do is to create a LinkedIn post about
3:03:04
agent development kit uh from the tutorial that I'm creating for you guys. So this is uh hey if you want to take a
3:03:10
moment to share the post that we're going to create mean the world to me and also like and subscribe all the goodness. And here are the requirements
3:03:17
for this post. You need to talk about how you are excited. here's everything that we covered in this tutorial so that
3:03:23
there are, you know, the agent knows exactly what we've worked on together. We're also saying here's the style requirements, no emojis, no hashtags.
3:03:30
And then finally, what I want you to do is only return the post. Don't do any additional commentary, and don't do any
3:03:37
formatting markers. Just give me the post, nothing else. And per usual, because we want to save the output of
3:03:43
this agent to state so that the next agents can use it. And that's where we're going to use our output key once
3:03:48
again to save it to state under current post. Great. So now let's look at uh the agents with inside of our loop agent. So
3:03:56
our loop agent, the first one that we always are going to do and trigger is going to be the post reviewer. So the
3:04:02
post reviewer, let's walk through these instructions carefully. First things first, we specified that the post we're
3:04:09
generating needs to be within a,00 to 1500 characters. So you need to use the
3:04:15
character count tool to make sure and check the post length. If it's too big, too small, we need to do another
3:04:20
iteration. So this is where we're just giving instructions on what to do if the length is too big or too small. From
3:04:26
there, if the length is correct, we then want to make sure that our post meets all of these criteria. So you want to
3:04:33
say it mentions my name, it has a clear call to action, shows genuine excitement, and once again, we want to
3:04:38
make sure that all of these different style requirements are met. If any of them don't pass, we need to say, "Hey,
3:04:45
something went wrong." And if something does go wrong for any specific reason, you need to return a concise
3:04:51
instructions on what went wrong. And then for whatever reason, if all of the requirements are met, if things go well,
3:04:58
I want you to call the exit loop function. And this exit loop function is the special case where we can actually
3:05:05
have our agent break out of the loop. So, what I want to do first is look at how we're going to count characters.
3:05:12
Then we're going to look at the exit loop so you can see how you can actually have your agents quit the loop. And then the only other thing I was going to
3:05:18
mention is obviously in order for us to review the agent, we need to access our current post in state. Okay, so let's go
3:05:24
look at our character count tool first. And as I mentioned a while ago, as you begin to build bigger and bigger agents,
3:05:31
you want to start to save your tools next to your agents in one nice tidy folder. So let's look at this. So in
3:05:37
this case, we're saying, all right, when it comes to the count character tool, I want you to give me the text and I want
3:05:44
the tool context. When it comes to, you know, looking at if the post is too big,
3:05:50
we're first just going to call length. This is a built-in Python function, and
3:05:55
we're going to look at the length of the entire post. If the length is too short, we're going to return a result saying,
3:06:02
"Hey, I sorry, we're going to say I failed." And the reason why is because my character count is too tiny. Here's
3:06:09
the current one. I need you add in an additional 20 characters. And then we're going to have a nice little message that
3:06:14
puts it all together where it says, "Hey, post is too short. Add this many characters. The minimum length is this."
3:06:19
So, we're just reminding the agent what it needs to do. If it was too big, what we're going to do is say, "Hey, you
3:06:26
know, you need to the post is too long. Remove this many characters. Here's the max length." So, that's all this tool
3:06:32
does. And outside of that, we're just updating the review status to fail if any of these requirements aren't
3:06:38
validated. Finally, if the post is not too big or too small, we're going to say everything was a pass. And we're going
3:06:44
to have this tool return a a message that says, "Yep, everything passed. Here's the character count, and
3:06:50
everything looked great." So that's what the character count tool is going to do. Now, we get to dive into the exit loop
3:06:57
functionality. And this is where you are going to have your agents say, "Life's
3:07:02
good. I'm happy with the result." Quit iterating and going over and over in the loop. So this is exactly what you need
3:07:08
to do. All you have to do is accessing the tool context that you can pass into
3:07:14
your tool calls. You are going to say tool context actions escalate. And escalate, all it does is it exits the
3:07:20
current loop. Super simple to use. And then you just return none. That's all you got to do. All right, great. So now
3:07:26
that you've seen how we can review a post, let's look at what happens if there is feedback. So we're now going to
3:07:32
go over to the post refiner agent who's responsible for taking in the input and acting on it. So we're going to say, all
3:07:39
right, you are the LinkedIn post refiner. Your job is to refine the LinkedIn post based on feedback I give
3:07:45
you. Here's the current post saved to state. And what I want you to do is look at the feedback that I've given you from
3:07:53
the previous agent. Because if you remember everything's getting saved to review feedback. So that's what we're
3:07:58
accessing right here. Now what we're saying when it comes to the actual task for this you know hey please apply the
3:08:04
feedback appropriately to improve the post. You know don't get wild don't change everything. Keep it as you know
3:08:10
similar as possible. Here's the requirements one more time as you're making the feedback changes and then go
3:08:15
from there. And the job is once it's done. So here's like where the loop happens. It's going to save the changes
3:08:21
it makes to current post. So what's happening is like first what's happening is like we generate the post from there
3:08:28
we are reviewing the post and then refining it and then I don't know why it's dropping away like that but once we
3:08:34
refine the post we're saving the results back to current post so that when we go to review it again we know exactly where
3:08:40
to look. Okay great hopefully this makes sense. So now that we've seen it all in the instructions let's run this bad boy
3:08:46
so you can see it in action. So let's clear everything out. We're going to make sure we change directories over to
3:08:53
the proper folder. So you need to be in the final example and you need to make sure our environment is activated. And
3:08:59
now we can run it. So we can just type in adk web and this will generate a post for us or sorry this will open up the
3:09:05
browser so that we can generate a post. So I'm going to say please generate a
3:09:11
post saying that this was the best ADK tutorial I've ever watched.
3:09:19
Now, what this is going to do, let's make this a little bit bigger for you guys. Now, we're going to generate this.
3:09:25
From there, what we would expect to see is our initial postgenerator agent go off and run. And
3:09:31
this is where it will make a initial rough draft of saying, "Hey, AI with Brandon did an awesome job. I learned a
3:09:38
ton." But you can see I'm going to let it run cuz it's it's doing its loop thing. Yeah. Okay. So, now we can start
3:09:43
to look at it. So, you can see it took its first attempt. It did a pretty good job. like this is a really nice looking
3:09:49
rough draft. Then we had our second agent start to go through and count
3:09:55
characters. So you can see at this point what's happening is we're at this step. So the initial post generator sorry yeah
3:10:01
the initial post generator already ran right here and now we are already in post refinement specifically we are
3:10:08
looking at the post reviewer and the post reviewer always counts characters and we can see oh it looks like this
3:10:14
post is too short. you need to add more details to meet the minimum length. From there, the refiner agent takes in all
3:10:22
the information and generates a much longer post. Except this time, it went way too hard. So, you can now see in the
3:10:28
count character tool, you know, hey, this post is way too long. You need to remove like almost half the characters.
3:10:34
This is crazy. So, then it does it again where this time it does a pretty much a lot better job. And this time, you can
3:10:41
see it counted the characters. Things are looking great. Now we are in a state
3:10:47
to where this post now basically this post reviewer so this is the output from
3:10:52
post reviewer it says this post mentions Brandon it talks about everything it needed to and then because everything
3:10:58
looked good we can now exit the loop so we should be able to see our final state
3:11:03
in here so if we go to state this is the final output of our agent where this
3:11:10
post has all the core requirements where it's not too long it's not too short and everything looks great. So you can see,
3:11:17
yep, this is so excited. It talks about everything, you know, I've been brainstorming. Yeah, everything about this post is just like what you would
3:11:24
need to do because it meets all our criteria. So yeah, that is our loop agents in a nutshell. And just a core
3:11:30
quick core reminder, the way it worked. So you remember the core lessons is loop agents will continually work until one
3:11:37
of two things happens. First, it will exit if we iterate too many times and it'll say, "Hey, I was unable to get you
3:11:43
the answer you wanted." Or option two is when the agent it does everything it was
3:11:48
supposed to and we call exit loop where all we do is escalate to say escalate true and we'll break out of the loop.
3:11:55
But yeah, you guys are now officially experts at working with all sorts of the different workflows and everything else
3:12:01
when it comes to creating ADK agents. And just a few quick reminders, you can download all the source code that you
Outro
3:12:06
saw today completely for free. Just click the link down the description below. Also, if you have any questions,
3:12:12
you can either drop a comment down below, or you can head over to the free school community I created for AI
3:12:17
developers just like you, where you can hop on our weekly free coaching calls and get direct feedback from me so we
3:12:22
can get you unstuck and moving forward. But that's for this video, guys, today. And I have a ton of other AI related
3:12:28
content on this channel and a bunch more tutorials coming out for more ADK content. Definitely recommend checking
3:12:34
out all the other videos I have and whichever videos are popping up right now on the screen. But until the next one, can't wait to see you guys. Have a
3:12:39
good one. Bye.

All

From the series

From aiwithbrandon