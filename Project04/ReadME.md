# Introduction
This project utilizes De Brujin graphs to reconstruct a genome. We were provided with a small subset of mouse genome, 10 million reads x 150 bps, and tasked to build a program that attempts to reassemble as much of the genome as we could. The program does not have implementation to handle genome variation. 

# Pseudocode
```
Load reads 
	Use read_fastq function to read in file 
        Only every 2nd of 4 lines will contain the sequence data	 
    Store in list format, each sequence as entry 

Build De Brujin graph 
	Initialize DeBruijnGraph class object for all of sequencing data 
		contains functions and variables for working with the graph object 
	Build graph: 
		for each read: (read two kmer-1s, add left kmer-1 as key and right kmer-1 into value list)* to end of read 

Assemble contigs: 
	Find start_nodes (nodes where outs – ins  = 1 or ins = 0)
    Run eulerian walk of graph =  
        starting at a start node,
        Choose random node to traverse 
        Remove edge
        move to next node
        return nodes if end is reached
        recurse if more nodes
    Reverse sequence from walking. Use first k-1mer as base, extend contig from last nucleotide of each following node 
Return contigs 

Write FASTQ and statistics to file using provided functions 
```

# Successes
Our team met several times over the weekend and quickly produced a working program. We all made sure the others understood each part of the program as we went through, and suggested improvements and helped with troubleshooting. 

# Struggles
Our main hurdle was the memory issue. Even with a subset we had to raise the python recursion limit in order to run at smaller k-mers. We could successfully get our code to quickly run for all 10 million reads at a k-mer length of 145, but no lower. Trying to lower the k-mer length quickly led to us either to hitting the recursive limit (even the higher limit), or running out of memory.  We did learn a lot from trying to make our code more efficient at this step, but eventually we could not make any more changes that would lead to meaningful improvements in memory use. 

# Personal Reflections
## Hongyuan Deng
Building the De Bruijn graph framework profoundly deepened my algorithmic thinking, and I truly enjoyed collaborating with my two teammates Nicholas and Victoria. I learned a lot from their clever optimizations(for instance, replacing my slow copy.deepcopy() with an efficient for loop.) Overall, this project was a fantastic lesson in both teamwork and memory management in Python.

## Nicholas Bottomley
Other members' reflections on the project

## Victoria Van Berlo
I enjoyed working with Hongyuan and Nicholas for this project. Recursion is very hard for me but my group members really helped me to understand how we could implement it. I gained practical experience with class objects as well as managing and organizing the many helper functions. I also learned a lot about Python memory use and improving speed due to our efforts to get the code to run in a reasonable amount of time and for lower k-mers.

# Generative AI Appendix
We used Claude Sonnet 4.6 in order to understands concepts related to memory overhead and to try to speed up the functioning program.
