// webpack.js

const path = require("path");

module.exports = {
    // ...
    resolve: {
        // ...
        alias: {
            "@src": path.resolve("src"),
        },
        // ...
    },
    // ...
};

// jest.config.js

module.exports = {
    // ...
    moduleNameMapper: {
        "^@src/(.*)$": "<rootDir>/src/$1",
    },
    // ...
};

module.exports = {
    // ...
    settings: {
        "import/resolver": {
            alias: {
                map: [["@src", "./src"]],
            },
        },
    },
    // ...
};


// jsconfig.json

{
    "compilerOptions": {
        "baseUrl": "./",
        "paths": {
            "@src/*": ["src/*"]
        }
    },
    "exclude": ["node_modules"]
}

