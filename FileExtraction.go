package main

import (
	"fmt"
	"os"
	"path/filepath"

)

func getFileInfoDict(path string) (map[string]map[string]interface{}, error) {
	fileInfoDict := make(map[string]map[string]interface{})

	err := filepath.Walk(path, func(file_path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}

		if !info.IsDir() {
			fileName := info.Name()
			fileSize := info.Size()
			modifiedTime := info.ModTime()

			fileInfo := map[string]interface{}{
				"file_path":     file_path,
				"file_size":     fileSize,
				"modified_time": modifiedTime,
			}

			fileInfoDict[fileName] = fileInfo
		}

		return nil
	})

	return fileInfoDict, err
}

func main() {
	currentDir, _ := os.Getwd()
	fileInfoDict, err := getFileInfoDict(currentDir)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	for key, value := range fileInfoDict {
		fmt.Printf("%s: %v\n", key, value)
	}
}
