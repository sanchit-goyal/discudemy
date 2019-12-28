// Code generated by protoc-gen-go. DO NOT EDIT.
// source: course.proto

package discudemy

import (
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

type Courses struct {
	Courses              []*Course `protobuf:"bytes,1,rep,name=courses,proto3" json:"courses,omitempty"`
	XXX_NoUnkeyedLiteral struct{}  `json:"-"`
	XXX_unrecognized     []byte    `json:"-"`
	XXX_sizecache        int32     `json:"-"`
}

func (m *Courses) Reset()         { *m = Courses{} }
func (m *Courses) String() string { return proto.CompactTextString(m) }
func (*Courses) ProtoMessage()    {}
func (*Courses) Descriptor() ([]byte, []int) {
	return fileDescriptor_ad75674299e1bb1e, []int{0}
}

func (m *Courses) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Courses.Unmarshal(m, b)
}
func (m *Courses) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Courses.Marshal(b, m, deterministic)
}
func (m *Courses) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Courses.Merge(m, src)
}
func (m *Courses) XXX_Size() int {
	return xxx_messageInfo_Courses.Size(m)
}
func (m *Courses) XXX_DiscardUnknown() {
	xxx_messageInfo_Courses.DiscardUnknown(m)
}

var xxx_messageInfo_Courses proto.InternalMessageInfo

func (m *Courses) GetCourses() []*Course {
	if m != nil {
		return m.Courses
	}
	return nil
}

type Course struct {
	Name                 string   `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
	Url                  string   `protobuf:"bytes,2,opt,name=url,proto3" json:"url,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *Course) Reset()         { *m = Course{} }
func (m *Course) String() string { return proto.CompactTextString(m) }
func (*Course) ProtoMessage()    {}
func (*Course) Descriptor() ([]byte, []int) {
	return fileDescriptor_ad75674299e1bb1e, []int{1}
}

func (m *Course) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Course.Unmarshal(m, b)
}
func (m *Course) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Course.Marshal(b, m, deterministic)
}
func (m *Course) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Course.Merge(m, src)
}
func (m *Course) XXX_Size() int {
	return xxx_messageInfo_Course.Size(m)
}
func (m *Course) XXX_DiscardUnknown() {
	xxx_messageInfo_Course.DiscardUnknown(m)
}

var xxx_messageInfo_Course proto.InternalMessageInfo

func (m *Course) GetName() string {
	if m != nil {
		return m.Name
	}
	return ""
}

func (m *Course) GetUrl() string {
	if m != nil {
		return m.Url
	}
	return ""
}

func init() {
	proto.RegisterType((*Courses)(nil), "discudemy.Courses")
	proto.RegisterType((*Course)(nil), "discudemy.Course")
}

func init() { proto.RegisterFile("course.proto", fileDescriptor_ad75674299e1bb1e) }

var fileDescriptor_ad75674299e1bb1e = []byte{
	// 121 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xe2, 0xe2, 0x49, 0xce, 0x2f, 0x2d,
	0x2a, 0x4e, 0xd5, 0x2b, 0x28, 0xca, 0x2f, 0xc9, 0x17, 0xe2, 0x4c, 0xc9, 0x2c, 0x4e, 0x2e, 0x4d,
	0x49, 0xcd, 0xad, 0x54, 0x32, 0xe3, 0x62, 0x77, 0x06, 0x4b, 0x15, 0x0b, 0x69, 0x73, 0xb1, 0x43,
	0x54, 0x15, 0x4b, 0x30, 0x2a, 0x30, 0x6b, 0x70, 0x1b, 0x09, 0xea, 0xc1, 0xd5, 0xe9, 0x41, 0x14,
	0x05, 0xc1, 0x54, 0x28, 0xe9, 0x71, 0xb1, 0x41, 0x84, 0x84, 0x84, 0xb8, 0x58, 0xf2, 0x12, 0x73,
	0x53, 0x25, 0x18, 0x15, 0x18, 0x35, 0x38, 0x83, 0xc0, 0x6c, 0x21, 0x01, 0x2e, 0xe6, 0xd2, 0xa2,
	0x1c, 0x09, 0x26, 0xb0, 0x10, 0x88, 0x99, 0xc4, 0x06, 0xb6, 0xd9, 0x18, 0x10, 0x00, 0x00, 0xff,
	0xff, 0xa9, 0xf8, 0xbf, 0xc9, 0x89, 0x00, 0x00, 0x00,
}