package main

import (
	"fmt"
	"net/http"
)

var taskItems = []string{"Task 2", "Task 3", "Task 4"}

func main() {
	// vars
	var taskOne = "Another task"
	taskSecond := "Example task"

	// array
	// in this example it has a max of 20 itens
	var taskItems2 = [20]string{taskOne, taskSecond}

	// prints
	fmt.Println("#### Welcome to our To Do List App! ####")
	fmt.Println("App created to improve Go knowledge")
	fmt.Println("List of To Do's")

	fmt.Println()
	fmt.Println("#### House ####")
	fmt.Println("Make lunch")
	fmt.Println("Clean the house")
	fmt.Println("Water the plants")
	fmt.Println(taskOne)
	fmt.Println(taskSecond)

	fmt.Println()
	fmt.Println("#### Dog ####")
	fmt.Println("Walk to the park")
	fmt.Println("Give a bath")
	fmt.Printf("This is %v\n", taskOne)

	fmt.Println()
	fmt.Println("#### Other tasks ####")
	fmt.Println("Tasks:", taskItems)
	fmt.Printf("Tasks: %v\n", taskItems2)

	for index, task := range taskItems {
		fmt.Printf("%d. %s\n", index+1, task)
	}

	// Start web server
	http.HandleFunc("/", helloUser)
	http.HandleFunc("/show-tasks", showTasks)
	http.ListenAndServe(":8080", nil)
}

func printTask(task string) {
	fmt.Println("Task:", task)
}

func addTask(newTask string) {
	taskItems = append(taskItems, newTask)
	fmt.Println("Added task:", newTask)
}

func helloUser(writer http.ResponseWriter, request *http.Request) {
	var greeting = "Hello user. Welcome to our Todolist App!"
	fmt.Fprintln(writer, greeting)
}

func showTasks(writer http.ResponseWriter, request *http.Request) {
	for _, task := range taskItems {
		fmt.Fprintln(writer, task)
	}
}