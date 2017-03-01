/*
   
  struct Node
  {
     int data;
     struct Node *next;
  }
*/

Node* Reverse(Node *head)
{   if (head!=nullptr)
    {
      Node *n=head;
      head =nullptr;
     while (n)
         {
         Node *m=n;
         n=n->next;
         m->next=head;
         head=m;
         
         
     }
}
    
    return head;

   
  // Complete this method
}

