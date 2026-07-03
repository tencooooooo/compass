import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  // GitHub Pagesのようなサブパス配信でも動くよう、アセットとデータは相対パスで参照します。
  base: "./",
  server: {
    port: 5174,
  },
});
