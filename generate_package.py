# Save this script in the same directory as your 'dir_structure.txt'
# Run it to generate a 'Package.swift' file based on your directory structure.

def main():
    with open('dir_structure.txt', 'r') as f:
        lines = f.readlines()

    sources = []
    tests = []

    for line in lines:
        line = line.strip()
        if '/Sources/' in line:
            sources.append(line.split('/Sources/')[1])
        elif '/Tests/' in line:
            tests.append(line.split('/Tests/')[1])

    with open('Package.swift', 'w') as f:
        f.write('// swift-tools-version:5.8\n')
        f.write('import PackageDescription\n')
        f.write('\n')
        f.write('let package = Package(\n')
        f.write('    name: "YourPackageName",\n')
        f.write('    dependencies: [\n')
        f.write('        .package(url: "https://github.com/onevcat/Kingfisher.git", from: "7.9.1"),\n')
        f.write('    ],\n')
        f.write('    targets: [\n')
        
        # Write sources
        f.write('        .target(name: "YourSourceTargetName", dependencies: [')
        for source in sources:
            f.write(f'"{source}",')
        f.write(']),\n')
        
        # Write tests
        f.write('        .testTarget(name: "YourTestTargetName", dependencies: [')
        for test in tests:
            f.write(f'"{test}",')
        f.write(']),\n')

        f.write('    ]\n')
        f.write(')\n')

if __name__ == '__main__':
    main()
