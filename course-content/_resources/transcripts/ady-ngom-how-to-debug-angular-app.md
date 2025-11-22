---
Title: "How to debug your Angular app with Chrome dev tools"
Published: September 19, 2022
View Count: 5,891
Subscribers: 1,690
---

# How to debug your Angular app with Chrome dev tools

## Transcript
[00:00] Hello, and welcome to angular recipe.  

[0:08] So today on the menu, we're going to be  talking about debugging your code in angular,  

[0:13] and I'm going to show you two ways of doing it  once inside of Chrome and the other one inside  

[0:19] of vs code. So first let me walk you through  the code that we're going to use as a sample.

[0:24] So here we have a setup where we have  an observable. That is getting some account info  

[0:32] and basically it's only gonna fire or it's only  gonna be active once it has an account status.  

[0:40] So we do have an interface here at the top showing  what type of things we expect in the acount info.  

[0:49] Okay. We have an inline template here that is,  I'm just basically going to switch from loading  

[0:56] to showing the account and the account number.

[0:58] Now to simulate this whole thing,  we have created two private functions. So we  

[1:05] have a transform function, which is the add  account statement -basically it will just  

[1:10] take the account and wrap this syntax around it,  but the most important one is the get account.  

[1:17] That we're calling here on line 39 and we are  using it to simulate a sequence basically.

[1:23] So we have a timer with the RxJs, um,  operator, and then basically every second it will  

[1:32] update the account, giving it the account type  first, the accounts services, the account number,  

[1:37] and last, the most important one for us, the  account status. So we remember that on the  

[1:43] filter it's not going to fire or it's not  gonna react until we get an account status.

[1:50] Okay. So. And at  the bottom of it real quick,  

[1:54] we have it here every single time. It's  just like, uh, reassigning the object  

[2:00] and then updating it with the new information that  it has here. So this is just done to simulate, um,  

[2:08] you know, a real life thing that I saw pretty  recently. So how would we go about this?

[2:12] So the problem we are looking at  this here, it's already running on 4,200 for us,  

[2:20] and it's just saying loading. And usually  when you have anything that is not working,  

[2:26] your very first thing is to go to inspect,  looking at the dev tool and going to the console.  

[2:33] And you seeing that there is no  errors, nothing is being thrown out.

[2:37] There is nothing. This code seems to  be clean. There's nothing here to help you. So  

[2:44] the very first thing that  we would do in this case,  

[2:48] We can say, okay. All right. We have a one-liner  here. Is this being fired at all? So let's expand  

[2:54] this and instead of just, uh, going for the truthy  value here, let's be a little more explicit.

[3:00] So I'm gonna copy account status.

[3:07] Actually I'm just going to cut it and  I'm just going to expand this expression here  

[3:13] and let me start and say that I'm going to have a  constant here that I'm going to call isTrue. Okay.  

[3:24] So is true, is going to be equal to this.  Okay. And then we're just going to return  

[3:34] east. All right. So now we kind of have  expanded, like I will filter logic here.

[3:40] And my very first reaction might be  to say, let's log this out. So let's log is true.

[3:52] True. Come in as, and then go back to  the. To our browser. We see that it's still not  

[4:02] firing. So the code looks clean. What is happening  here? Um, so if you already spotted the error,  

[4:09] uh, great. But let's just pretend that we have  to go through the steps to try to understand  

[4:14] what's going on. So the filter, um, we just  saw that it never gets to this point now.

[4:23] We have our simulator  function here. Private get account.  

[4:28] Do we get anything going on here? So same thing.  

[4:32] Let's have we have new object? Let's try to  log it out. Okay. So let's log new object.

[4:43] All right. And still nothing. So it  tells me that basically this entire code block  

[4:54] is not being fired. So the problem  here, it might be very subtle.  

[5:01] If you have been using RSGS and observable for  while it might just be very obvious to you,  

[5:08] but we have put together like this observer and  every. But we're not subscribing to anything.

[5:14] So basically if you  have this map, uh, operator here,  

[5:20] uh, it's never going to this entire team is never  going to get fired at any point, because we don't  

[5:26] have a subscription. So it's like, why do I have  to work if I don't have anybody to show my work.  

[5:33] So to prove the point that  the consoles are not working.

[5:37] So let's just add. Just to prove  the point real quick. We're not going to be  

[5:43] critical about the structure of this. We  can, we factor this in an added episode,  

[5:47] but today we're just going to do the  debugging. So my assumption is that  

[5:51] it's missing like a subscribed block. Okay.  So I'm just gonna turn on a subscribe here.

[5:58] Actually, we have to put  it in the right spot because I'm still  

[6:02] under the operators, the tear down. So at the end  of the. Operator, I'm going to add my subscribe.  

[6:11] Okay. And honestly, I don't even have to do  anything the moment that I'm going to put  

[6:15] in that, in there, it's going to  say to the observer, Hey, wake up.

[6:19] There's somebody like listening to  you, so, okay. Go and sing your song or whatever,  

[6:24] do whatever I have to do. So right now doing  this, I'm going to assume that my. Statements  

[6:31] are going to start firing and you see them.  I have about four or five statements because  

[6:36] we are in a loop where account number  basically gets set up every single time.

[6:42] And we have like false, false, false.  And finally, that's true. And if we look at  

[6:47] what the true is, and that's going to be inside  the filter, all right. That is great. So how can  

[6:56] we, uh, have a better strategy about debugging  this whole thing? So we see that, um, The console  

[7:06] logs are pretty good, but they don't really  tell you the history of things, how they happen.

[7:12] And like the sequencing of when  you are having like something like a stream,  

[7:18] um, uh, over time, how is this going on?  Like, is it ever going to be true? Is it  

[7:24] going to be false all the time? Those  are not going to be caught by just a  

[7:28] simple console log. So we're going  to be using what are called breaks.

[7:32] We're going to be using breakpoints  and we're going to set them up in Chrome first.  

[7:36] And then afterwards, we're going  to do the same thing in a vs code.  

[7:40] So to do that, usually when I come into  a project and I have a lot of files,  

[7:45] I'm just kind of trying to figure out what's  going on. I might not go to vs code first.

[7:49] I might just copy the name of the  function or something that makes sure that  

[7:55] I'm going to catch this function. I'm going  to copy this and let's go back to Chrome.  

[8:03] And what I'm going to do real quick.  Let's get a read of the consult statement.  

[8:09] Actually, I'm going to leave them  there. They're not hurting at all.

[8:12] Um, let's do this and let's come back  to our source. We are already there and in here.  

[8:24] If you come to sources, you're going to have  all the JavaScript and CSS that is on the  

[8:28] page. Basically, you're going to have them do not  module the SRC, the Webpack, everything. And then  

[8:34] we want to be searching all those files by right  clicking on the top here and searching all file.

[8:41] And here we're going to paste the  search, which is private, get account info.  

[8:48] And we want to get, if you Indev mode, you want to  get to the. That is right. You know, um, uh, that  

[8:55] you are looking at in your ID. So this is the  one I want to be playing with. Okay. Cause you  

[9:03] might get the Webpack version too. So that's not  what we interested in, at least not for today.

[9:07] So we see that the line numbers are the  same. This is, this is very important. So I know  

[9:13] that online 66. Yeah. So I'm looking  at the, the file that I want to edit,  

[9:20] right. Like in the Chrome browser. Okay. So I  can get rid of this hour real quick and what  

[9:26] I'm going to do. The same thing, basically, I'm  going to start putting some break points here.

[9:31] Okay. So if there are highlighted, that  means that they are active. So I have like this,  

[9:37] uh, break point. I have a second break point  here. So I want to see if it is returning  

[9:42] something or not. And at filter, let's go  to the filter. But one for the line 43.  

[9:55] And let's see, let's put a final  one here for the account info.

[10:02] So basically what I'm trying to  get to is okay. Um, is this being called?  

[10:10] What is the value? Cause when I go to the return  statement is going to do every single time. It  

[10:15] looks. It's going to show me the values so I  can see the sequence. And then here filter,  

[10:23] basically it should stay false until it gets  to the point where we have an account status.

[10:30] And when that account status is  true, then it started like firing the rest  

[10:35] of the tear down here, which is we're going  to take it only once we are going to do a  

[10:40] little transform and we're going to return the  account. Okay, so let's go ahead and just refresh  

[10:47] our browser. And you're going to see  that our break points are firing now.

[10:53] So console that log, new object and  new object, you see that we have an account, um,  

[10:59] object, but only residential has a value. Okay.  So now once we are here, we can go to the next  

[11:08] from here. Which is just going to go to the  next slide. And then it's just going to give  

[11:13] us again new objects. Now, if we want  to go to our next break point is true.

[11:20] Coming here is going to be false.  So anything that is going to be here should  

[11:25] not be fired anything inside of the tear down,  because since it's false, take one should not  

[11:32] be active and the maps should not be active. So  we cannot expect to have something online. 50.  

[11:39] So, if I do this, it's just going to go all the  way back to our function and the new object.

[11:47] This time has account services  that is on and has account type residential  

[11:52] that was on. And then you see that  loop continues. We go back to filter  

[11:59] and filter is still false. That's what we  expecting. Okay. The next one, this time  

[12:06] is going to set up, um, the account number, but  account status is still no. So, so far so on.

[12:16] And then we come back is true. It's  going to be false because we still don't have  

[12:20] an account status. Now, finally, when we get to  the last one and then we have an account status.  

[12:30] It's going to jump to filter and it's true. This  time is going to be true. Now our break point  

[12:36] online 52 should fire because now the condition,  the predicate that we had in filter is true.

[12:43] So now it's going  to let it go through. Okay.  

[12:47] And you see now when we go to line 52, this time  we have the account info with all the information,  

[12:54] but the most important part is the account status  is. Okay, this is what we want it. And if we take  

[13:01] out subscribe, then we're going to  have a problem. So let's keep going.

[13:05] And then here now, instead of  just having something that is saying loading,  

[13:11] the transformation that we have here on line  50 has been applied, and then we have account  

[13:18] showing with the proper account number. All  right. So we went through that within, uh,  

[13:24] Chrome, and you can see how this is  very powerful because not only you  

[13:31] kind of see what is going on in your, in,  in your logic, but in almost real time.

[13:36] You can see the sequencing and  see, uh, at every single state of that logic,  

[13:43] what are the values and so forth and so on. And  one thing that I forgot to show you is here in  

[13:50] the Chrome dev tools. If you expand this  because it's going to be important when we  

[13:58] go back to Vieques code, if you expand  this, let me refresh this real quick.

[14:04] You're going to see that,  uh, it's going to give you the variables  

[14:10] and the context within the context where you are.  So lapsed right now is at one. What is labs? Labs?  

[14:20] Labs is right here. And it's telling  you that we are now at index number one,  

[14:25] labs is at one because we already started here  

[14:28] and then it's going to be showing you the local  variable that is going to be available right here.

[14:34] [00:14:28] So you can, you have even, uh, some  watch expression. You can add some stuff in there.  

[14:39] So looking at the scope, you see that, and as  I'm going through, okay. Every single time,  

[14:47] wherever it is, wherever your Brooke breakpoint  is, is going to give you the value of the  

[14:52] variables that are around. So here it's giving  you basically, you know, those value here.

[14:57] [00:14:52] This is very valuable. It, it tells you  

[15:00] in real time how your object, how your  state is changing. Okay. And finally,  

[15:06] I'm just not gonna do go through the whole thing.  Let's just get to the point where laps this time,  

[15:12] it's going to be equal to two and so forth and  so on. So I wanted to show you this because.

[15:18] [00:15:12] Imagine now that you had to come  to Chrome to get this experience, and then  

[15:25] depending on your setup, you know, you might not  have enough. I highly recommend that you have more  

[15:30] than one school. If you're going to be doing a  lot of debugging and stuff. And just in general,  

[15:35] as a developer, probably have a second screen, but  let's say we wanted to recreate this environment,  

[15:42] doing the same exact thing without having to leave  our favorite ID in my case, which is vs code.

[15:49] [00:15:44] Okay. So first let me get rid of  the break points. You can do it either here,  

[15:56] or you can just come back here and get rid of  all those breakdowns. Okay now just to make sure  

[16:06] all my breakpoints are off.  I don't want to have any on,  

[16:12] okay. Let me refresh. Yeah, we should just  get to 1, 2, 3, 4 seconds and it gets there.

[16:20] [00:16:14] Perfect.

[16:21] [00:16:16] Let's do the same thing  now using VS Code. So in VS Code,  

[16:21] Before we go there, there is a page called  vs code recipes that is put out by Microsoft,  

[16:21] and we're going to be looking closely at  the angular CLI res recipe. This is going  

[16:21] to allow us or help us to debug our angular  CLI application. Um, I believe that vs code,  

[16:21] uh, if you have the latest, if you go  to your extension, The GSD debugger is,  

[16:21] uh, cause in some, the videos, you might  hear people talking about Chrome debugger.

[16:21] [00:16:55] You don't need to do that anymore  because I believe that the JSD burger is built in,  

[16:21] um, is it called jazz debugger or GS debug,  something like that. Anyways, the thing is,  

[16:22] um, they do have that. And you don't  have to install anything. It comes  

[16:22] with the latest version of vs. Good.  Okay. So now what I'm going to do is

[16:22] [00:17:24] the recipe basically has like,  we already have an angular application and  

[16:22] everything. So the thing is we're going to  have to create what is called a launch. Jeez,  

[16:22] Jason file. Most of the time, you're going  to have a dat vs code for. And in this,  

[16:22] that Viscoat folder, we just have an  extension. Jason, we don't have anything else.

[16:22] [00:17:46] Okay. So now what are we going  to do? We want to run and debug inside the  

[16:22] vs code. So we have the run and debug, uh,  option right here. So let's go ahead. And  

[16:22] the moment we create, uh, or we just  like click on running debug is going  

[16:22] to like have this window and we want  to be able to do that debug in Chrome.

[16:22] [00:18:07] Okay. So it creates a lounge, Jason  file for us. And then it says based on like,  

[16:22] uh, our environment is going to say like  the type and then the type of request,  

[16:23] which is just going to launch a new window  and then the name. So the name that you see  

[16:23] here is the name that is in here basically, but  let's go back to the recipes and they basically.

[16:23] [00:18:36] Ask you to copy this for the angular  CLI and start here. So I'm going to copy it. Come  

[16:23] back to the idea. And pasted over here. Okay.  What is important here? So there is a pre-launch  

[16:23] task. You can read more about it. It's pretty  straightforward. I was able to pretty much,  

[16:23] I'm not a big conflict guy and I was pretty  much able to figure out pretty quickly,  

[16:23] but the most important part  here is the prelaunch task is  

[16:23] saying that it's going to target  an NPM and then the start script.

[16:23] [00:19:10] So let's open our package, Jason.

[16:23] [00:19:17] And then you have a start script  here, so it will be targeting the start script  

[16:23] and we'll just do NGS. Okay. But if it does NG  serve that way, it's going to serve it with the  

[16:23] default. And you might not want to be running  your, your, your, your, your debugging, um,  

[16:24] on your 4,200 port, you might be having a select  port that you want to use for your debugging.

[16:24] [00:19:39] So what are we going to do? Let's go  back to the recipes. They do have a secondary  

[16:24] file here called task, and then we're going  to copy this and that's tasked with. So be,  

[16:24] be very careful to name it,  uh, tasks with an S Jason,  

[16:24] we're going to come back here and, uh, in the  dat vs code. So this is where it should exist.

[16:24] [00:20:02] That vs code. We're going to add  a new file and we're gonna call it task. And  

[16:24] it's important that you put it in the plural  because that's one is going to be looking for.  

[16:24] And then we're just going to pay. Uh, what  we have in there. So you see that the type  

[16:24] NPM and the script start, this is, this is  matching what we have in our pre-launch.

[16:24] [00:20:26] So now what I want to do is I'm going  to create a new script and I'm going to call  

[16:24] it start debug. Okay. And instead of going to a  4,200, I wanted to go to port 92. There you go.  

[16:25] And while we here instead of the name, just seeing  NG serve. Um, so if I come here, the running the  

[16:25] button, now that I have, um, um, instead of saying  just NG serve, what is the name of this project?

[16:25] [00:21:00] This project's name is debug  angular. I'm going to call it debug angular,  

[16:25] sir. Not debug, debug angular serve. Okay, let  me copy this command. Copy. Let me save it. And  

[16:25] you see now that I have debug angular serve.  Now I'm going to do the same thing for tests,  

[16:25] even though I'm not going to  show test today and end to end.

[16:25] [00:21:31] Command V command. As now in my  dropdown here, I have the book angular serve,  

[16:25] divert angular test, and then the  book angular eat to eat. If you want,  

[16:25] you can have the serve before, so  you don't have to have the dropdown  

[16:25] telling you in which one you are, but I'm  okay with this. So. Now I wanted to have,  

[16:25] uh, as the target start debug, but  the start debug doesn't exist yet.

[16:25] [00:21:59] So I'm going to go back to my, uh,  first, I mean, launch Jason. I'm going to go  

[16:26] to my task, Jason, and instead of script start,  I'm going to have strip start debug. All right.  

[16:26] Finally, in my package, Jason. Let's just  copy this line and pace it, come and see,  

[16:26] come. And V if you're on the mat and then I'm  going to add, start debug and under serve here.

[16:26] [00:22:27] I wanted to go to port 9,200, not  93, 9200. There you go. Now my setup is ready.  

[16:26] I went to vs. Code a recipe. I got my lounge,  Jason. I mean, I got, I copied a launch, Jason,  

[16:26] which after I, uh, fired up here, my running  debug, I copied over, I did the same thing  

[16:26] with task Jason. And now I have a dedicated script  that is just going to run NG, serve on port 9,200.

[16:26] [00:23:01] And that's going to be my debug  session since this is, since it is going  

[16:26] to launch a whole new. Okay. So after all  of this is done, after the setup is done,  

[16:26] now I can come make sure that I'm in depth,  debug, English serve, and I'm just gonna click  

[16:26] play. Okay. So you see that now we have,  this is going to do NPR, man, start debug,  

[16:26] and then it's going to do the NG serve on  port 9,200, which is exactly what I wanted.

[16:27] [00:23:28] Okay. So let's give it a second  here. And you're going to see in a second,  

[16:27] why this whole setup like is so important why  we are going through this whole trouble. All  

[16:27] right. We have all of that compiled successfully.  Great. And now you see that is showing angular,  

[16:27] um, in this new, um, browser it's like  local host, 9,200, uh, let's expand on.

[16:27] [00:24:02] Okay. And, um, now we don't even  need to use the council here cause we're going  

[16:27] to do the same thing we were doing exactly in  Chrome. So let's go back. Let's collapse this  

[16:27] to give us some space. And let's do the same  with this. Let's give us some more space here  

[16:27] and I'm going to go back to app component and  I'm going to put my first break point here now.

[16:27] [00:24:32] Return new object like we had  earlier. So that's my first break point.  

[16:27] Then I'm going to go to field. Return is  true. I'm going to put my second break  

[16:27] point. Okay. Now when I do this and  I go back to 9,200 and I refresh it,  

[16:28] you're going to see that my breakpoints  get fired up and I'm right inside of VSL.

[16:28] [00:24:59] And you see here, look, we have,  the variable labs is at zero right now. The  

[16:28] new object only has residential setup as we  are expecting. So now I can walk through,  

[16:28] I can either go to my next break point  or I can step over or I can step into,  

[16:28] so let's go to the next break point, which  is returned is true. And then it's true.

[16:28] [00:25:23] Here is going to be for.  It's going to be undefined. Okay. So  

[16:28] as I hovered through you see that is true, is  false just by hovering over. You see that now  

[16:28] you have this information, but at the same  time here, like you had in the browser,  

[16:28] you have the variables in the context  you're in. So let's keep on going.

[16:28] [00:25:49] It comes back to new object.  This time lapse is equal to. Okay. And  

[16:28] it's true. It's still going to be false  and you're still going to see that. Um,  

[16:28] um, we don't have, um, we don't have anything  for account status, but we do have something  

[16:29] for account services. So it is doing the  right sequence, like what we were expecting.

[16:29] [00:26:19] Okay. So real quick, uh, labs equal  to. Return here is true. It's still going to  

[16:29] be false. We have the setup here. Everything is  here, but we don't have an account status yet.  

[16:29] And then finally, if we go one more time,  now this time is true. Is true. And here,  

[16:29] since I'm at vs. Good. Let me put like  real quick, one more break point here.

[16:29] [00:26:51] And then when I hit it, it's  going to come here right there. Okay.  

[16:29] So I should have have this break point  in the, in the beginning and then now,  

[16:29] but I'm in vs code. I can even add stuff  as I'm doing this. I can add them in real  

[16:29] time. I can debug in real time, I can  change the code in real time and still  

[16:29] that functionality with the break points, the  debugging, everything is going to be there.

[16:29] [00:27:14] So you see that we have accounting.  And then if I look here now I have an account  

[16:29] info with everything in it now. So as  I'm walking through this in my browser,  

[16:30] it's still pending and loading because it  has to come through here first, then go  

[16:30] to the subscribed block. So let's do something.  Let's do a subscriber, is going to give us data.

[16:30] [00:27:42] And then here. Let's  just, uh, console that log the data.

[16:30] [00:27:57] There we go and then let's add  a break point for it. So brand new break  

[16:30] point. It might not. You might have, if  we do this, sometimes you might have to  

[16:30] restart because this is kind of like one  of the only part where Visco doesn't shine,  

[16:30] because it's going to be like a disconnected  break point, but you get the idea.

[16:30] [00:28:18] So let me just save this. Let's see,  there you go. After saving it. I can add my  

[16:30] break point. I'm going to just fast forward  to the point where it's going to hit data.

[16:30] [00:28:34] Return is true. Now we have returning  this account info and we expecting it to get into  

[16:30] our subscribed block, which is Daz. And when it  does, when it does this, when you go back here,  

[16:30] And finally you hit your final break point.  Now you have the account number showing up  

[16:31] without a problem. So, yeah, so it's  a little extensive show of two ways.

[16:31] [00:29:02] One, I mean, essentially one  way, but in two different like medium one  

[16:31] directly inside of Chrome. And you have  a lot of things that you can do there,  

[16:31] like with the dev tools. And there's a  dedicated tool called like the Angelo  

[16:31] dev tools that you might want to look into.  If you want to take it a step further, that  

[16:31] was one that was released by the angular team,  but that's the recipe that we had for you today.

[16:31] [00:29:28] And I see you soon for the next.
