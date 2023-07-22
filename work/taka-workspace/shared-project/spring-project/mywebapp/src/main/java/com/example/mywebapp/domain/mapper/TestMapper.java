package com.example.mywebapp.domain.mapper;

import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

@Mapper
public interface TestMapper {

  String selectTest(@Param("name") String name);
}