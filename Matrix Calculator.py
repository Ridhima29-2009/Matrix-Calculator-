import numpy as np

A = np.array([
    [10, 20],
    [30, 40]
])

B = np.array([
    [5, 15],
    [25, 35]
])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nShape of Matrix A:")
print(A.shape)

print("Shape of Matrix B:")
print(B.shape)

print("\nSize of Matrix A:")
print(A.size)

print("Size of Matrix B:")
print(B.size)

print("\nDimensions of Matrix A:")
print(A.ndim)

print("Dimensions of Matrix B:")
print(B.ndim)


# Matrix Operations

print("\nA + B:")
print(A + B)

print("\nA - B:")
print(A - B)

print("\nMatrix Multiplication (A @ B):")
print(A @ B)

print("\nElement-wise Multiplication (A * B):")
print(A * B)

print("\nMatrix Division (A / B):")
print(A / B)


# Matrix Statistics

print("\nSum of Matrix A:")
print(np.sum(A))

print("\nSum of Matrix B:")
print(np.sum(B))

print("\nMean of Matrix A:")
print(np.mean(A))

print("\nMean of Matrix B:")
print(np.mean(B))

print("\nMaximum of Matrix A:")
print(np.max(A))

print("\nMaximum of Matrix B:")
print(np.max(B))

print("\nMinimum of Matrix A:")
print(np.min(A))

print("\nMinimum of Matrix B:")
print(np.min(B))


# Row-wise Operations

row_sum_A = np.sum(A, axis=1)
print("\nRow-wise Sum of Matrix A:")
print(row_sum_A)

row_mean_A = np.mean(A, axis=1)
print("\nRow-wise Mean of Matrix A:")
print(row_mean_A)

row_sum_B = np.sum(B, axis=1)
print("\nRow-wise Sum of Matrix B:")
print(row_sum_B)

row_mean_B = np.mean(B, axis=1)
print("\nRow-wise Mean of Matrix B:")
print(row_mean_B)


# Column-wise Operations

column_sum_A = np.sum(A, axis=0)
print("\nColumn-wise Sum of Matrix A:")
print(column_sum_A)

column_mean_A = np.mean(A, axis=0)
print("\nColumn-wise Mean of Matrix A:")
print(column_mean_A)

column_sum_B = np.sum(B, axis=0)
print("\nColumn-wise Sum of Matrix B:")
print(column_sum_B)

column_mean_B = np.mean(B, axis=0)
print("\nColumn-wise Mean of Matrix B:")
print(column_mean_B)


# Searching

position_of_40 = np.where(A == 40)
print("\nPosition of 40 in Matrix A:")
print(position_of_40)

position_of_15 = np.where(B == 15)
print("\nPosition of 15 in Matrix B:")
print(position_of_15)


# Sorting

sorted_A = np.sort(A.flatten())
print("\nSorted Elements of Matrix A:")
print(sorted_A)

sorted_B = np.sort(B.flatten())
print("\nSorted Elements of Matrix B:")
print(sorted_B)


# Final Report

print("\n========== Matrix Calculator ==========")

print("Matrix A Shape:", A.shape)
print("Matrix B Shape:", B.shape)

print("\nAddition:")
print(A + B)

print("\nSubtraction:")
print(A - B)

print("\nMatrix Multiplication:")
print(A @ B)

print("\nAverage of Matrix A:", np.mean(A))
print("Average of Matrix B:", np.mean(B))

print("\nMaximum Value in A:", np.max(A))
print("Minimum Value in A:", np.min(A))

print("\nMaximum Value in B:", np.max(B))
print("Minimum Value in B:", np.min(B))

print("\n=======================================")