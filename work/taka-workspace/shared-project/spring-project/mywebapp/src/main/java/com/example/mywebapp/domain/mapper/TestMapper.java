package com.example.mywebapp.domain.mapper;

import com.example.mywebapp.domain.entity.TestEntity;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

@Mapper
public interface TestMapper {

  TestEntity selectTest(@Param("name") String name);
}