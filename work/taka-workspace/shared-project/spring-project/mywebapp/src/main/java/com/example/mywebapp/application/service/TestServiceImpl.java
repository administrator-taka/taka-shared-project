package com.example.mywebapp.application.service;

import com.example.mywebapp.infrastructure.logic.TestLogic;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Transactional
@Service
@RequiredArgsConstructor
public class TestServiceImpl implements TestService {

  private final TestLogic testLogic;

  @Override
  public void test(String name) {
    System.out.println("name:" + name);
    testLogic.test(name);
  }
}
