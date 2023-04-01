package main

import (
    "fmt"
    "math/rand"
    "time"
)

// List of departments that can use the name generator
var allowedDepartments = []string{"Marketing", "Accounting", "FinOps"}

func generateUniqueNames() {
    // Input name of department and validate
    var deptName string
    fmt.Print("Please enter the name of your department: ")
    fmt.Scanln(&deptName)
    allowed := false
    for _, department := range allowedDepartments {
        if deptName == department {
            allowed = true
            break
        }
    }
    if !allowed {
        fmt.Println("Sorry, You need secret security to access this information.")
        return
    }

    // Input number of instances && validate if it's a number
    var numInstances int
    for {
        fmt.Print("Hello, please enter the number of EC2 instances you need names for: ")
        _, err := fmt.Scanln(&numInstances)
        if err == nil {
            break
        }
        fmt.Println("Sorry, the input must be a numberic value. Please try again.")
    }

    // Generate unique names for each instance
    rand.Seed(time.Now().UnixNano())
    for i := 0; i < numInstances; i++ {
        randomString := make([]byte, 7)
        for j := range randomString {
            randomString[j] = byte(rand.Intn(36) + 65)
            if randomString[j] >= 91 {
                randomString[j] -= 26
            }
        }
        uniqueName := fmt.Sprintf("%s-%s", deptName, string(randomString))
        fmt.Println(uniqueName)
    }
}

func main() {
    generateUniqueNames()
}