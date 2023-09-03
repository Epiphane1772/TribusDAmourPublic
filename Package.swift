// swift-tools-version:5.7.1
import PackageDescription

let package = Package(
    name: "YourPackageName",
    dependencies: [
        .package(url: "https://github.com/onevcat/Kingfisher.git", from: "7.9.1"),
    ],
    targets: [
        .target(name: "YourSourceTargetName", dependencies: ["main.swift",]),
        .testTarget(name: "YourTestTargetName", dependencies: []),
    ]
)
