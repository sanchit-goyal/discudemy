package main

import (
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	ioutil "io/ioutil"
	discudemy "github.com/sanchit-goyal/discudemy/proto"
)

const (
	jsonFileName = "src/github.com/sanchit-goyal/discudemy/files/discudemy.json"
	protoFileName = "src/github.com/sanchit-goyal/discudemy/files/discudemy.proto.obj"
)
	

func readFromProto() discudemy.Courses{
	in, err := ioutil.ReadFile(protoFileName)
	if err != nil {
		fmt.Println(err)
	}
	courses := &discudemy.Courses{}
	if err := proto.Unmarshal(in, courses); err != nil {
		fmt.Println(err)
	}
	return *courses
}

func writeToProto() {
	courses := &discudemy.Courses{
		Courses: []*discudemy.Course{
			{Name: "name", Url: "URL"},
		},
	}
	fmt.Println(courses)
	fmt.Println(proto.Marshal(courses))
}

func main() {
	courses := readFromProto()
	fmt.Printf("value := %v, length := %d\n", courses.GetCourses(), len(courses.GetCourses()))
	writeToProto()
}
