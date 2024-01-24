#include <stdio.h>
#include <string.h>

/* a simple program that takes two strings as input and compares them to check if they match */

/* ideas for improvement:
    - have program analyze what hashes are given */

int main()
{
    char hash1[516], hash2[516];
    // take input hashes as strings with bits limit
    printf("Insert first hash: ");
    fgets(hash1,516,stdin);
    printf("Insert second hash: ");
    fgets(hash2,516,stdin);

    // compare the two inputs and output accordingly
    if (strcmp(hash1,hash2) == 0) {
        printf("VALID MATCH\n");
}   else {
        printf("INVALID MATCH\n");
}
    return 0;
}