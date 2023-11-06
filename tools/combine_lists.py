def combine_lists(list1_file, list2_file, output_file):
  """Combines the content of two lists in two different files into a third list in a separate file.

  Args:
    list1_file: The path to the file containing the first list.
    list2_file: The path to the file containing the second list.
    output_file: The path to the file where the combined list should be saved.
  """

  # Read the contents of the two files into lists.
  list1 = []
  with open(list1_file, "r") as f:
    for line in f:
      list1.append(line.strip())

  list2 = []
  with open(list2_file, "r") as f:
    for line in f:
      list2.append(line.strip())

  # Combine the two lists into a third list.
  combined_list = list1 + list2

  # Remove duplicate items from the combined list.
  combined_list = set(combined_list)

  # Write the combined list to the output file.
  with open(output_file, "w") as f:
    for item in combined_list:
      f.write(item + "\n")


if __name__ == "__main__":
  # Get the paths to the input and output files from the user.
  list1_file = input("Enter the path to the first list file: ")
  list2_file = input("Enter the path to the second list file: ")
  output_file = input("Enter the path to the output file: ")

  # Combine the two lists and save the results to the output file.
  combine_lists(list1_file, list2_file, output_file)

  # Print a message to the user indicating that the script has finished executing.
  print("The combined list has been saved to the file:", output_file)
