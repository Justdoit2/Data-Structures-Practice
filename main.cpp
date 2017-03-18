//
//  main.cpp
//  Hackerank
//
//  Created by Alma Niu on 3/18/17.
//  Copyright © 2017 csciClass. All rights reserved.
//Insert value at head of linked list
#include <iostream>


using namespace std;
struct Node {
    int data;
    struct Node *next;
};

Node*Insert(Node *head,int data)
{
    Node*front=new Node();
    front->data=data;
    front->next=head;
    head=front;
    return head;
}


