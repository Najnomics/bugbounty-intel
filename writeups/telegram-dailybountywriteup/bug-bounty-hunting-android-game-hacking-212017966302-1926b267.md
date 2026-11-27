# Android Game Hacking

- **Source URL:** https://medium.com/bug-bounty-hunting/android-game-hacking-212017966302?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142612/https://medium.com/bug-bounty-hunting/android-game-hacking-212017966302
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4154 (id 4154)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Android Game Hacking 101

This post will cover basic tips and tricks to get started into android game hacking and using game guardian tool and others.

## Client Side Games

Most games are client sided since server sided game are costly/latency issues.

## Some Ways:

- Memory editing and others

Under these most popular tools are Game Guardian, Lucky Patcher (4.2,.3X v) , Game Killer , Sb game Hacker tool, Cheat engine , Freedom etc.

Freedom Tool ?

Mimics Playstore purchases.

Mostly works in Android 6 or \<

Google’s SafetyNet Attestation API to check if device has tampered. If the device is not certified by Google, the game will not be launched. (But magisk has bypass for them)

- Changing values stored at client side

**Hxd Tool**

helps to change values stored in .json and .xml files

## Common Games are:

Most games are unity-based.

Reverse Engineering:

## dnSPY ?

Efficient windows based .net compiler

How to check for for variables/ obfuscation is proper or not ?

- Use APK EASY tool / others to decompile apk.
- Import Assembly-CSharp.dll file
- We can search for functions which generate coins etc and try to modify them and recompile the apk back.
- (Require some knowledge of assembly instructions..)

## Game Guardian Techniques

- Game Guardian is most efficient memory editing tool.

**Game guardian bypass on prod till v164 Using virtually exposed(Ali)**

Below are the steps to bypass the app guard :

1. Root the mobile.
2. Install custom rom (google search for mobile device) \< android 10
3. Install Magisk + custom recovery orange fox
4. Now, Delete the magisk apk
5. Lets, install the Magisk apk (\<=22 version)
6. Change name of magisk (Settings -> hide magisk from all the app)
7. Shield Icon -> hide all libraries of the app

## How GG works?

- End goal is reach upto the memory value which stores the score/points/life by search.

## VALUE TYPES

- *DWORDs*

Basic numbers . Storage size for DWORD type is 4 bytes.

- *FLOAT*

1.5, 2.6 etc

- *DOUBLE*

Same as floats, but it can store much larger values

- XORs

Type of encryption

- WORDs

Same as DWORD, but store much smaller numbers (2 bytes),

- BYTEs

Same as DWORD, but only one byte is reserved for the value.

- QWORDs

Similar to **DWORD** with bigger storage size.

- **Most common value type while searching is DWORD .**
- If we are unable to find values, we can use **AUTO but this will take more time and give huge results.**

SPEED HACK:

TIME HACK:

Only works if game uses android clock time

SEARCHING KNOWN VALUES

Use the search and select type as Dword, continue searching and refining until we get less memory values which will lead to right address.

OVERWRITING VALUES EXAMPLE:

FREEZE VALUES:

SEARCHING FOR ENCRYPTED VALUES

UNKNOWN FUZZY SEARCH:

## GROUP SEARCH IN GG

- Two or more values that are close to each other.
- Helpful in speeding search

SYNTAX-

**VALUE1;VALUE2;VALUE2:RANGE**

Ex. Life= 100, Score=50

100;50:200

This will search for values that 100 and 50 values which are 200 address from each other.

## Basic encryption

Addition , Division, Multiplication, Subtraction by random values .

For example score is 50.

Simple encryption is addition by 25.

So in memory value would be 75.

So we can edit value as 125 and in game value will be changed to 100.

## XOR encryption

- **1 XOR 1 = 0**
- **1 XOR 0 = 1**
- **0 XOR 1 = 1**
- **0 XOR 0 = 0**

Different Values= 1

Similar Values= 0

Working to check in-built XOR encryption in Game guardian when 444444 doesn’t works

## GG Custom Lua Script

We can create menu etc.

From 2018, we can record our actions and save it as script and then load it back.

Sample example of recorded lua script:

```
-- options
local scriptName = [=====[Script for QA Pro 1.0.167_development_qa_20220224_10_18]=====]
local scriptVersion = '1.0.0'
local scriptAuthor = 'User'
local startToast = ''
-- 0 - no check; 1 - check package only, 2 - check package and build
local checkTarget = 0
local targetName = [=====[ QA Pro]=====]
local targetPkg = 'com.qa.androidapp'
local targetVersion = [=====[1.0.167_development_qa_20220224_10_18]=====]
local targetBuild = 1000167
-- functions
-- init
gg.require('101.1', 16142)
if startToast ~= '' then startToast = '\\n'..startToast end
gg.toast(scriptName..' v'..scriptVersion..' by '..scriptAuthor..startToast)
if checkTarget ~= 0 then
 local info = gg.getTargetInfo()
 local check = false
 local current = false
 if checkTarget >= 1 then
  check = targetPkg
  current = info.packageName
 end
 if checkTarget >= 2 then
  check = check..' '..targetVersion..' ('..targetBuild..')'
  current = current..' '..info.versionName..' ('..info.versionCode..')'
 end
 if check ~= current then
  gg.alert('This script for "'..targetName..'" ['..check..'].\\nYou select "'..info.label..'" ['..current..'].\\nNow script exit.')
  os.exit()
 end
end
local revert = nil
-- main code
gg.searchNumber("100", gg.TYPE_DWORD, false, gg.SIGN_EQUAL, 0, -1, 0)
gg.processResume()
gg.refineNumber("99", gg.TYPE_DWORD, false, gg.SIGN_EQUAL, 0, -1, 0)
revert = gg.getResults(100, nil, nil, nil, nil, nil, nil, nil, nil)
local t = gg.getResults(100, nil, nil, nil, nil, nil, nil, nil, nil)
for i, v in ipairs(t) do
 if v.flags == gg.TYPE_DWORD then
  v.value = "100"
  v.freeze = true
 end
end
gg.addListItems(t)
t = nil
gg.processResume()
```
**POINTER SEARCH in GG:**

Pointers point from one address to another address from where the instructions jumps to and starts its execution from there.

In GG, change value format to “QWORD”, and all violet addresses are pointers.

Basic Scenario:

a) Login Reward Day 1 points to = 100 gold

b) Login Reward Day 2 points to = 200 gold.

We can change the pointer in a) to target to the reward of 200 gold of the second pointer and in this way we can get 200 gold in the first day itself.

*Pointers may or may not work from game to game .*

Watch this video for more details

**OFFSETS IN GAME GUARDIAN**

In a nutshell, offsets are the distance b/w two values.

Main advantage of offset is that we can search for values faster

Sample demo:

1. Search for a value in game guardian.
2. Use Go To to go the memory address.
3. We see lot of hex address formats.

Offset value b/w 00000004 and 00000000 is 4.

Usually in game , multiple values are stored nearby to each other.

For example if the gold value is stored in hex address 00000004, there is a possibility that score value might be stored in nearby hex addresses to it, ex. at 00000000.

So now, if we search for the value of gold in GG, we can apply offset 4 , and quickly reach the address which stores the score value too!

Video Tutorial:

## Server Side Games

Games can be either entirely be on server / important variable like coin/time can be synced at server side.

- Memory editing can be easily detected.
- Hacking server side can be only done via edge cases and varies differently with each game .

Ex. Attacker disconnects internet and updates score, at the same time, due to bad implementation of code , server may fetch and store the newly updated score due to low network latency.

Some recent fraud with regard to disconnection of opponent from the game.

How hackers hack server sided games?

They simply have private copied servers with unlimited life/ammo for all players. These are usually unofficial.

## CUSTOM ENCRYPTION

Each company may implement its own custom encryption logics which may be seen using adb logcat. Here a sample script for the same.

Useful script to double check custom encryption implementation while testing.

```
#!/bin/bash
echo "Checking for Fraud Instrumentation Proof"
time=$(date "+%Y.%m.%d-%H.%M.%S")
#adb logcat -s Unity 2>&1 | tee ${time}.txt  adb logcat -s Unity > ${time}.txt 2>&1 &
#touch ${time}.txt
echo "Waiting for 10 mins for log generation"
sleep 600
grep " SFS2X fraud detected" ${time}.txt | head -n 1
grep " Memory Injection Detected" ${time}.txt | head -n 1
grep " Hack detected" ${time}.txt | head -n 1
```
PS: Instrumentation is being changed occasionally , so grep value would have to be changed in future.
