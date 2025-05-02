import { readFileSync } from "fs";
import { codegen } from "swagger-axios-codegen";

const swaggerDocument = JSON.parse(
  readFileSync("./swagger.json", "utf-8")
);

codegen({
  methodNameMode: "operationId",
  source: swaggerDocument,
  outputDir: "./api",
});
