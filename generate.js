const fs = require('fs-extra')
const glob = require('tiny-glob')
const { render } = require('nunjucks')
const providers = require('./providers')

glob('src/**/*.py').then(paths => {
  for (let name of Object.keys(providers)) {
    const NAME = name.toUpperCase()

    for (let path of paths) {
      const file = path.replace(/^src/, `api/${name}`)

      fs.outputFileSync(file, render(path, {
        ...providers[name],
        fname: name,
        NAME
      }))
    }
  }
})
