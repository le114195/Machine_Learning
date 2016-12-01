#include<iostream>



int main()
{
    int x, y;
    
    FILE *pfile=fopen("ticdata1.txt","wb");
    
    //第一象限
    for (int i = 0; i < 1000; i++) {
        x = rand() % 100;
        y = rand() % 100;
        
        fprintf(pfile, "%d      %d      1\n", x, y);
    }
    
    //第二象限
    for (int i = 0; i < 1000; i++) {
        x = -rand() % 100;
        y = rand() % 100;
        
        fprintf(pfile, "%d      %d      2\n", x, y);
    }
    
    //第三象限
    for (int i = 0; i < 1000; i++) {
        x = -rand() % 100;
        y = -rand() % 100;
        
        fprintf(pfile, "%d      %d      3\n", x, y);
    }
    
    //第四象限
    for (int i = 0; i < 1000; i++) {
        x = rand() % 100;
        y = -rand() % 100;
        
        fprintf(pfile, "%d      %d      4\n", x, y);
    }
    
    
    fclose(pfile);
    return 0;
}
