package com.example.mywebapp.infrastructure.logic;

import com.example.mywebapp.domain.entity.TestEntity;
import com.example.mywebapp.domain.mapper.TestMapper;
import com.example.mywebapp.infrastructure.model.TestModel;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Component;

@Component
@RequiredArgsConstructor
public class TestLogic {

  private final TestMapper testMapper;

  public TestModel test(String name) {
    TestEntity entity = testMapper.selectTest(name);
    TestModel model = new TestModel();
    model.setId(entity.getId());
    model.setName(entity.getName());
    model.setPassword(entity.getPassword());
    return model;

  }

}
