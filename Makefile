run:
	  @python scrape.py > recentrun.txt #send scrape.py output to file
	  @sh run.sh #run shell script to diff files
	  @cp recentrun.txt archive.txt #archie recentrun.txt for future execution
