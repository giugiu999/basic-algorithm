#include <stdio.h>
#include <stdlib.h>

#define MAX_NODES 1000

int nodes[MAX_NODES] = {0}; // index <-> id, if exists the value is 1; otherwise 0
int **edges; // edges[i]是一个指针，指向动态分配的边数组
int **weights; // weights[i]是一个指针，指向动态分配的权重数组
int *num_edges; // 记录每个节点的边数量

// TODO: Implement these functions
int nodeExists(int id);
int edgeExists(int source_id, int dest_id);
int insertNode(int id);
int insertEdge(int source_id, int dest_id, int weight);
int removeEdge(int source_id, int dest_id);
int removeNode(int id);
int path(int source_id);
void start();
void end();
void start() {
    for (int i = 0; i < MAX_NODES; i++) {
        nodes[i] = 0;
    }

    edges = (int **)malloc(MAX_NODES * sizeof(int *));
    weights = (int **)malloc(MAX_NODES * sizeof(int *));
    num_edges = (int *)calloc(MAX_NODES, sizeof(int)); // 初始化为0

    for (int i = 0; i < MAX_NODES; i++) {
        edges[i] = (int *)calloc(MAX_NODES, sizeof(int)); // 初始化为0
        weights[i] = (int *)calloc(MAX_NODES, sizeof(int)); // 初始化为0
    }
}

// 结束函数
void end() {
    for (int i = 0; i < MAX_NODES; i++) {
        free(edges[i]);
        free(weights[i]);
    }
    free(edges);
    free(weights);
    free(num_edges);
}
int nodeExists(int id) {
    if (id < 0 || id >= MAX_NODES) {
        return 0; // invalid id
    }
    return nodes[id];
}
int edgeExists(int source_id, int dest_id) {
    if (source_id < 0 || source_id >= MAX_NODES || dest_id < 0 || dest_id >= MAX_NODES) {
        return 0; // invalid source or destination
    }
    return edges[source_id][dest_id]; // return 1 if edge exists, otherwise 0
}
int insertNode(int id) {
    if (id < 0 || id >= MAX_NODES) {
        return 0; // invalid id
    }
    if (nodes[id]) {
        return 0; // node already exists
    }
    nodes[id] = 1; // mark node as existing
    return 1; // successfully inserted
}
// 插入或更新边
int insertEdge(int source_id, int dest_id, int weight) {
    if (source_id < 0 || source_id >= MAX_NODES || dest_id < 0 || dest_id >= MAX_NODES) {
        return 0; // 无效的源或目标
    }
    if (source_id == dest_id) {
        return 0; // 不允许自连接
    }
    if (!nodes[source_id] || !nodes[dest_id]) {
        return 0; // 源或目标节点不存在
    }

    if (edges[source_id][dest_id] == 0) { // 如果边不存在，则增加边计数
        num_edges[source_id]++;
    }
    
    edges[source_id][dest_id] = 1; // 标记边存在
    weights[source_id][dest_id] = weight; // 更新边的权重
    return 1; // 成功插入或更新
}

// 移除边
int removeEdge(int source_id, int dest_id) {
    if (source_id < 0 || source_id >= MAX_NODES || dest_id < 0 || dest_id >= MAX_NODES) {
        return 0; // 无效的源或目标
    }
    if (!edges[source_id][dest_id]) {
        return 0; // 边不存在
    }
    
    edges[source_id][dest_id] = 0; // 移除边
    num_edges[source_id]--; // 减少边计数
    return 1; // 成功移除
}
int removeNode(int id) {
    if (id < 0 || id >= MAX_NODES || !nodes[id]) {
        return 0; // node does not exist
    }
    nodes[id] = 0; // remove node
    // remove all edges associated with this node
    for (int i = 0; i < MAX_NODES; i++) {
        edges[id][i] = 0; // remove all edges from this node
        edges[i][id] = 0; // remove all edges to this node
    }
    return 1; // successfully removed
}
int path(int source_id) {
    int totalWeight = 0;
    int id;

    // 从输入中读取后续节点
    while (scanf("%d", &id) == 1) {
        if (id < 0 || id >= MAX_NODES) {
            return -1; // invalid node ID
        }
        if (!nodes[source_id] || !nodes[id] || !edges[source_id][id]) {
            return -1; // path does not exist
        }
        totalWeight += weights[source_id][id]; // accumulate edge weight
        source_id = id; // update source node
    }
    return totalWeight; // return total weight
}
// ! DO NOT EDIT THE MAIN FUNCTION
int main(int argc, char **argv)
{
    start();
    
    // Input loop
    int result;
    while (1)
    {
        char command;
        scanf("%c", &command);

        if (command == 't')
        {
            break;
        }
        else if (command == 'n')
        {
            int id;
            scanf("%d", &id);
            result = nodeExists(id);
            printf("%d\n", result);
        }
        else if (command == 'e')
        {
            int source_id, dest_id;
            scanf("%d %d", &source_id, &dest_id);
            result = edgeExists(source_id, dest_id);
            printf("%d\n", result);
        }
        else if (command == 'i')
        {
            int id;
            scanf("%d", &id);
            result = insertNode(id);
            printf("%d\n", result);
        }
        else if (command == 'l')
        {
            int source_id, dest_id, weight;
            scanf("%d %d %d", &source_id, &dest_id, &weight);
            result = insertEdge(source_id, dest_id, weight);
            printf("%d\n", result);
        }
        else if (command == 'd')
        {
            int id;
            scanf("%d", &id);
            result = removeNode(id);
            printf("%d\n", result);
        }
        else if (command == 'r')
        {
            int source_id, dest_id;
            scanf("%d %d", &source_id, &dest_id);
            result = removeEdge(source_id, dest_id);
            printf("%d\n", result);
        }
        else if (command == 'p')
        {
            int source_id;
            scanf("%d", &source_id);
            result = path(source_id);
            printf("%d\n", result);
        }
    }

    end();
    return 0;
}
