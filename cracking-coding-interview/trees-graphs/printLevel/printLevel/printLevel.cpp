// printHorizontalLevel.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <list>
#include <stddef.h>
#include <math.h>

using namespace std;


//-----------------------------------------------------------------------
// Node of tree
template <typename T>
struct node
{
	node *l , *r;
	T data;
};

//-----------------------------------------------------------------------

// Create a node of a binary tree
template <typename T>
node<T>* createNode(T a)
{
	node<T>* t = new node<T>;
	t->data = a;
	t->l = NULL;
	t->r = NULL;
	return t;
}

// Build a binary tree
template <typename T>
node<T>* buildTree()
{
	node<T>* root = createNode<T>(1);
	root->l = createNode<T>(2);
	root->r = createNode<T>(3);
	root->l->l = createNode<T>(4);
	root->l->r = createNode<T>(5);
	root->l->l->l = createNode<T>(6);
	return root;
}


//-----------------------------------------------------------------------
/*
Print tree each horizontal level at a time recursion function
*/
template <typename T>
void printHorizontalLevel(node<T>* t)
{
	vector < list <node<T>*> > levelLists;
	printHorizontalLevel(t, levelLists, 0);

	for(size_t i = 0; i < levelLists.size() ; i++)
	{
		for( auto it = levelLists[i].begin(); it != levelLists[i].end(); it++)
		{
			node<T>* currNode = *it;
			cout<<currNode->data <<"  ";
		}
		cout<<"\n";
	}
}

/*
Print tree each horizontal level at a time recursion function
*/
template <typename T>
void printHorizontalLevel( node<T>* t, vector< list< node<T>* > > &levelLists, int level )
{
	if(t==NULL) return;

	if ((int)levelLists.size() > level)
	{
		levelLists[level].push_back(t);
	}
	else
	{
		list<node<T>*> nextLevel;
		nextLevel.push_back(t);
		levelLists.push_back(nextLevel);
	}
	printHorizontalLevel(t->l , levelLists, level+1);
	printHorizontalLevel(t->r , levelLists, level+1);
}


//-----------------------------------------------------------------------

/*
Print tree each vertical level at a time wrapper function
*/
template <typename T>
void printVerticalLevel(node<T> * t)
{
	vector < list <node<T>*> > levelListsRight;
	vector < list <node<T>*> > levelListsLeft;

	printVerticalLevel(t, levelListsLeft, levelListsRight, 0);


	for(int i = (int)levelListsLeft.size()-1; i>=0 ; i--)
	{
		for( auto it = levelListsLeft[i].begin(); it != levelListsLeft[i].end(); it++)
		{
			node<T>* currNode = *it;
			cout<<currNode->data <<"  ";
		}
		cout<<"\n";
	}

	for(size_t i = 0; i < levelListsRight.size() ; i++)
	{
		for( auto it = levelListsRight[i].begin(); it != levelListsRight[i].end(); it++)
		{
			node<T>* currNode = *it;
			cout<<currNode->data <<"  ";
		}
		cout<<"\n";
	}
}


/*
Print tree each vertical level at a time recursion function
*/
template <typename T>
void printVerticalLevel(node<T> *t, vector < list <node<T>*> > &leftList, vector< list< node<T>* > > &rightList, int pos)
{
	if (t==NULL) return;

	if(pos>=0)
	{
		if((int)rightList.size()>pos)
		{
			rightList[pos].push_back(t);
		}
		else
		{
			list<node<T>*> newList;
			newList.push_back(t);
			rightList.push_back(newList);
		}
	}
	else
	{
		int absPos = abs(pos)-1;
		if((int)leftList.size()>absPos)
		{
			leftList[absPos].push_back(t);
		}
		else
		{
			list<node<T>*> newList;
			newList.push_back(t);
			leftList.push_back(newList);
		}

	}
	printVerticalLevel(t->l, leftList, rightList, pos-1);
	printVerticalLevel(t->r, leftList, rightList, pos+1);
}




//-----------------------------------------------------------------------

void main()
{
	//Build tree
	node<int> *t = buildTree<int>();

	// Print the tree each horizontal level in a line
	cout<<"Printing horizontal Level : \n";
	printHorizontalLevel(t);


	// Print the tree each vertical level in a line
	cout<<"Printing Vertical Level : \n";
	printVerticalLevel(t);

	char c;
	cout<<"Enter any character : ";
	cin>>c;
}

//-----------------------------------------------------------------------
