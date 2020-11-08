#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define PARENT(i) (i>>1)
#define LEFT(i) (i<<1)
#define RIGHT(i) ((i<<1)+1)

typedef struct
{
    unsigned int index;
    char value;
}INDEX_VALUE;

// 维护最小堆
void min_heapify(INDEX_VALUE *heap, unsigned int i, unsigned int heap_size)
{
    unsigned int left = LEFT(i);
    unsigned int right = RIGHT(i);
    unsigned smallest = i;
    if (left < heap_size && heap[left].value < heap[i].value)
        smallest = left;
    if (right < heap_size && heap[right].value < heap[smallest].value)
        smallest = right;

    if (smallest != i)
    {
        INDEX_VALUE tmp = heap[i];
        heap[i] = heap[smallest];
        heap[smallest] = tmp;
        
        min_heapify(heap, smallest, heap_size);
    }
}

// 构建最小堆
void build_min_heap(INDEX_VALUE *heap, unsigned int heap_size)
{
    for (int i = (heap_size-1)>>1; i >= 0; i--)
    {
        min_heapify(heap, i, heap_size);
    }
}

#define SEQ 2
#define NUM 5
#define HEAP_SIZE 3
void main()
{
    // 构建数据
    // srand(time(NULL));
    char data[SEQ][NUM];
    for (int i = 0; i < SEQ; i++)
    {
        for (int j = 0; j < NUM; j++)
        {
            data[i][j] = rand()%256 - 128;
        }
    }

    printf("==== build data ====\n");
    for (int i = 0; i < SEQ; i++)
    {
        for (int j = 0; j < NUM; j++)
        {
            printf("%4d ", data[i][j]);
        }
        printf("\n");
    }
    printf("\n");


    // 初始化最小堆
    unsigned int heap_size = HEAP_SIZE;
    INDEX_VALUE min_heap[SEQ][HEAP_SIZE];
    for (int i = 0; i < SEQ; i++)
    {
        for (int j = 0; j < HEAP_SIZE; j++)
        {
            min_heap[i][j].index = j;
            min_heap[i][j].value = data[i][j];
        }
    }

    printf("==== init min heap ====\n");
    for (int i = 0; i < SEQ; i++)
    {
        for (int j = 0; j < HEAP_SIZE; j++)
        {
            printf("%4d:%4d ", min_heap[i][j].index, min_heap[i][j].value);
        }
        printf("\n");
    }
    printf("\n");

    // topk
    for (int i = 0; i < SEQ; i++)
    {
        build_min_heap(min_heap[i], heap_size);
        for (int j = HEAP_SIZE; j < NUM; j++)
        {
            if (data[i][j] > min_heap[i][0].value)
            {
                min_heap[i][0].value = data[i][j];
                min_heap[i][0].index = j;
                min_heapify(&min_heap[i][0], 0, heap_size);
            }
        }
    }

    printf("==== output min heap ====\n");
    for (int i = 0; i < SEQ; i++)
    {
        for (int j = 0; j < HEAP_SIZE; j++)
        {
            printf("%4d:%4d ", min_heap[i][j].index, min_heap[i][j].value);
        }
        printf("\n");
    }
    printf("\n");
}