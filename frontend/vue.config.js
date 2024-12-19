  const { defineConfig } = require('@vue/cli-service')
  module.exports = defineConfig({
    transpileDependencies: true,
    devServer: {
      host: '0.0.0.0', // Berjalan di host 127.0.0.1 dan di 192.168.x.x
      port: 8080, // Berjalan di port
      hot: true, // HMR memungkinkan pembaruan tanpa perlu memuat ulang seluruh halaman
      https: true,
      client: {
        overlay: { // Menampilkan overlay di browser ketika ada kesalahan atau peringatan
          errors: true,  // Menampilkan overlay untuk error
          warnings: false,  // Tidak menampilkan overlay untuk peringatan
        }
      },
      proxy: {
      '/l': {
        target: 'http://38.22.104.156:1170/api',
        changeOrigin: true
      },
      '/getTeachersViewPageData': {
        target: 'http:38.22.104.156:1170/api',
        changeOrigin: true
      },
    }
  }
})
