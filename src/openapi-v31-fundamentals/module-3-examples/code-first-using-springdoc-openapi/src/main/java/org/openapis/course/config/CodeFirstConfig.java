package org.openapis.course.config;

import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.info.Info;

import org.springdoc.core.customizers.OpenApiCustomizer;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class CodeFirstConfig {

  @Bean
  public OpenAPI customOpenAPI(@Value("${application-description}") String appDesciption,
      @Value("${application-version}") String appVersion) {
    return new OpenAPI()
        .info(new Info()
            .title("OpenAPI v3.1 Fundamentals Example")
            .version(appVersion)
            .description(appDesciption));
  }

  @Bean
  public OpenApiCustomizer additionalPropertiesCustomizer() {
    // Set additionalProperties to false for all Schema Objects
    return openApi -> openApi.getComponents().getSchemas().values().forEach(s -> s.setAdditionalProperties(false));
  }

}
