# Capture Replay Class
<p>
This is the Github repository for the TVVS class about Capture Replay.<br>
This readme explains how to setup things that are needed for the class.
</p>


## Setup
<p>
First, some of the tools require Java, so be sure to have JDK/JRE 7 or 8 installed on your computer. You can get it from http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html.
</p>
<p>
<b>For the class exercise, you will only need SikuliX</b>, but we also present installation instructions below for other tools that will be presented, if you want to experiment with them.
</p>

### Badboy
<ul>
  <li>Download the installer at: http://www.badboy.com.au/download. It should ask you some information, but you can skip it. Select the most recent version to download;</li>
  <li>Execute the downloaded file to install (.exe only, sorry to the mac users :( )</li>
  <li>When completed, go to "C:\{ Your Program Files folder }\Badboy";</li>
  <li>Execute "badboy.exe" to start Badboy.</li>
</ul>

### SikuliX
<ul>
  <li>Download it at: https://launchpad.net/sikuli/sikulix/1.1.0 (under "Download files for this release", the "sikulixsetup-1.1.0.jar" file);</li>
  <li>Before executing "sikulixsetup-1.1.0.jar", create a folder right on your C: or D: disk (like "C:\Sikuli" or "D:\Sikuli"), ensuring the path to it includes no whitespaces. This folder should not have any writing restrictions;</li>
  <li>Move/copy the "sikulixsetup-1.1.0.jar" to this folder and execute it;</li>
  <li>Select options "Pack1" and "Pack2", and click "Setup Now";</li>
  <li>Allow some time for it to download and install the selected packs, confirm when prompted during installation;</li>
  <li>To open SikuliX IDE, execute "sikulix.jar", "SikuliX.exe" (Windows), or "Sikulix.app" (Mac).</li>
</ul>

### Ranorex
<ul>
  <li>Ranorex is paid, but an evaluation version can be downloaded at: http://www.ranorex.com/;</li>
  <li>Provide the required information, and allow it to install.</li>
</ul>

<br>
<p>For more information, feel free to contact <b>ribeiro.pinto@fe.up.pt</b>.</p>

## Exercise Instructions

### A. Building the script

<ul>
  <li>In your browser, open the example page at http://jtrpinto.github.io/badboy/bbc_complete.html;</li>
  <li>This page simulates a situation of registration in a club;</li>
  <li>The page presents alerts in several situations:
    <ul>
    <li>(a) The user did not accept the rules;</li>
    <li>(b) The user did not fill all the required fields;</li>
    <li>(c) The specified name was a number;</li>
    <li>(d) The specified age was not a number;</li>
    <li>(e) The specified country was a number;</li>
    <li>(f) Everything is correct;</li>
    </ul>
  </li>
  <li>Using SikuliX, you should build a script with 7 tests: The first to ensure every element in the page is presented, and each of the other 6 to ensure the alerts are presented for each of the situations described above in (a)-(f);</li>
  <li>After building the script, refresh the page and run it to make sure it works (it shouldn't present any error, make sure to use if conditionals to avoid the script from stopping before the end).</li>
</ul>

### B. Checking on a flawed site

<ul>
  <li>In chrome, open a new page at jtrpinto.github.io/badboy/bbc.html;</li>
  <li>Run the script with this page open;</li>
  <li>Verify the results of the tests (3 of them should fail).</li>
</ul>
