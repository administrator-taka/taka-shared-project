package com.example.mywebapp.infrastructure.logic;

import com.example.mywebapp.domain.mapper.TestMapper;
import com.example.mywebapp.infrastructure.model.TestModel;
import javax.sql.DataSource;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import org.mybatis.spring.boot.test.autoconfigure.MybatisTest;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.io.ClassPathResource;
import org.springframework.jdbc.datasource.init.ResourceDatabasePopulator;
import org.springframework.test.context.jdbc.Sql;

@MybatisTest
class TestLogicTest {

  @Autowired
  private TestMapper testMapper;

  @BeforeAll
  public static void createDB(@Autowired DataSource dataSource) {
    ResourceDatabasePopulator populator = new ResourceDatabasePopulator();
    populator.addScript(new ClassPathResource("/sql/create_tbl.sql"));
    populator.execute(dataSource);
  }

  @Test
  @Sql("/sql/test.sql")
  public void test() {
    TestLogic testLogic = new TestLogic(testMapper);
    TestModel model = testLogic.test("testA");
    System.out.println(model);
  }
}