# Input number of rows
rows = int(input("Masukkan jumlah baris: "))

# Loop to print the pyramid
for i in range(1, rows + 1):
    # Print spaces
    print(" " * (rows - i), end="")
    
    # Print stars
    print("* " * i)
