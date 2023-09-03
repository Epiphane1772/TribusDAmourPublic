// swift-tools-version:5.8.0

import PackageDescription

let package = Package(
    name: "tribusdamourpublic",
    products: [
        .library(
            name: "tribusdamourpublic",
            targets: ["TribusDAmour"]),
    ],
    dependencies: [
        // Add your package dependencies here, if any.
    ],
    targets: [
        .target(
            name: "TribusDAmour",
            dependencies: [],
            path: "Sources/TribusDAmour")  // Replace this with your custom path if needed
    ]
)
