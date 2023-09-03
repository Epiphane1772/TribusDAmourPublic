// swift-tools-version:5.7.1
import PackageDescription

let package = Package(
    name: "tribusdamourpublic",
    products: [
        .library(name: "TribusDAmour", targets: ["TribusDAmour"]),
    ],
    targets: [
        .target(
            name: "TribusDAmour",
            path: "Sources/TribusDAmour"
        ),
    ]
)
