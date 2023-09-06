local null_ls = require('null-ls')

local opts = {
  sources = {
    null_ls.builtins.formatting.autopep8,
    null_ls.builtins.formatting.isort,
    null_ls.builtins.diagnostics.flake8,
    null_ls.builtins.formatting.clang_format,
    null_ls.builtins.formatting.cmake_format,
  }
}
return opts
