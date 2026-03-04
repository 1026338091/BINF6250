# Introduction
Description of the project

# Pseudocode
Put pseudocode in this box:

**Dynamic Scoring Strategy**

**Calculate the Scoring Matrix**
```
1. Calculate diagonal Score by adding match/mismatch score to the matrix[i-1][j-1]
2. Calculate the up score by adding the gap penalty to the matrix[i-1][j]
3. Calculate the left score by adding the gap penalty to the matrix[i][j-1] score in the matrix
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
3. While matrix[i][j] != 0:
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
Description of the team's learning points

# Struggles
Description of the stumbling blocks the team experienced

# Personal Reflections
## Group Leader
Group leader's reflection on the project

## Other member
Other members' reflections on the project

# Generative AI Appendix
As per the syllabus
