package com.example.mywebapp.infrastructure.logic;

import com.example.mywebapp.domain.entity.TestEntity;
import com.example.mywebapp.domain.mapper.TestMapper;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Component;

@Component
@RequiredArgsConstructor
public class TestLogic {

  private final TestMapper testMapper;

  public void test(String name) {
    TestEntity test = testMapper.selectTest(name);
    System.out.println("mapperの結果");
    System.out.println(test);
  }

}
