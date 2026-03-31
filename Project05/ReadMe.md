# Introduction
This project focuses on dynamic programming through the implementation of the Smith-Waterman algorithm for local sequence alignment. The algorithm builds a scoring matrix using match, mismatch and gap penalties, where each cell is calculated from the values above, left and diagonally above-left. After filling the matrix, the highest score is identified and a traceback step is performed to reconstruct the optimal local alignment between the sequences. 

# Pseudocode

**Dynamic Scoring Strategy**
```
Initialization
1. rows = length(seq1) + 1
2. columns = length(seq2) + 1 
3. Initialize scoring matrix of size rows x cols with 0
4. Initialize traceback matrix of size rows x cols with 0
5. max_score = 0
6. max_position = (0,0)

Iteration (Fill in Scoring Matrix)
7. For i from 1 to rows - 1
  	For j from 1 to columns - 1
      Compute score and direction  
    	Set scoring_matrix[i][j]  = score
    	Set traceback_matrix[i][j] = direction
  	
    	if score is greater than or equal to max_score
    		max_score = score
    		max_position = (i,j)
	
Traceback
8. Perform traceback starting from max_position 
8. Return aligned_seq1, aligned_seq2, and and score matrix
	
	

```

**Calculate the Scoring Matrix**
```
1. Calculate diagonal Score by adding match/mismatch score to the scoring_matrix[i-1][j-1]
2. Calculate the up score by adding the gap penalty to the scoring_matrix[i-1][j]
3. Calculate the left score by adding the gap penalty to the scoring_matrix[i][j-1] score in the matrix
4. Find the maximum of {0, diagonal, up, left}
5. Determine the direction corresponding to the maximum score
6. Return the score and its direction
```

**Traceback**
```
Initialization
1. Initialize aligned_seq1 and aligned_seq2 as empty lists
2. Initialize i and j to maximum position

Iteration
3. While traceback_matrix[i][j] != 0:
  	if direction is diagonal 
      append seq1[i-1] to aligned_seq1
      append seq2[j-1] to aligned_seq2
      i = i - 1
      j = j - 1 
  	
  	Else if direction is up
      append seq1[i-1] to aligned_seq1
      append gap to aligned_seq2
      i = i - 1	
  	
  	Else if direction is left
      append gap to aligned_seq1
      append seq2[j-1] to aligned_seq2
      j = j -1

4. Reverse aligned_seq1 and aligned_seq2
5. Return the aligned sequences as a string
```

# Successes
Each member of our team had prior exposure to the Smith-Waterman algorithm which made it easier for us to understand the concepts of the project. Handling the scoring, traceback directions and tracking the highest score was more straightforward for us because of this. Overall, we were able to implement the algorithm efficiently and it reinforced our understanding of the concept. 


# Struggles
Compared to the previous projects this one felt more straightforward conceptually. The idea of local alignment was clear to us which reduced confusion during implementation. We just had to be careful with indexing details and matrix boundaries. Overall, this assignment was relatively more simple and straightforward and we were able to implement it without too many obstacles or struggles.

# Personal Reflections
## Group Leader
Implementing the Smith-Waterman algorithm from scratch was a major technical breakthrough for me. Bridging my agricultural background with newly acquired coding skills, I successfully translated complex dynamic programming and traceback logic into functional Python. This project solidified my algorithmic foundation and gave me the confidence to tackle real-world computational biology challenges.

## Other member
Chantera - Both Hongyuan and Meghana were great to work with. As we all have implemenmted this particular algorithm prior to this class, implementation seemed straight forward. I think it gave me more time to digest dynamic programming conceptually.

Meghana - Personally, I found this concept easier than the other projects because I had previous experience with dynammic programming. This background helped me focus more on implementing the algorithm efficiently and the actual coding aspect of the project instead of spending more time trying to understand the theory.

# Generative AI Appendix
No
