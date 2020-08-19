'''
You are given a list of projects and a list of dependencies (which is a list of pairs of
projects, where the second project is dependent on the first project). All of a project's dependencies
must be built before the project is. Find a build order that will allow the projects to be built. If there
is no valid build order, return an error.


By the way, this problem is called topological sort:
linearly ordering the vertices in a graph such that for every edge (a, b),
a appears before b in the linear order.
'''


def find_build_order(projects, dependencies):
    build_order = []
    project_graph = create_graph(projects, dependencies)

    while project_graph:
        projects_with_depen = get_projects_with_dependencies(project_graph)
        projects_wo_depen = get_projects_wo_dependencies(
            projects_with_depen,
            project_graph
        )

        if len(projects_wo_depen) == 0 and project_graph:
            raise ValueError('There is a cycle in the build order')

        for independent_project in projects_wo_depen:
            build_order.append(independent_project)
            del project_graph[independent_project]

    return build_order

def get_projects_with_dependencies(graph):
    projects_with_depen = set()
    for project in graph:
        projects_with_depen = projects_with_depen.union(set(graph[project]))

    return projects_with_depen


def get_projects_wo_dependencies(projects_with, graph):
    projects_wo_dependencies = set()

    for project in graph:
        if not project in projects_with:
            projects_wo_dependencies.add(project)

    return projects_wo_dependencies

def create_graph(projects, dependencies):
    project_graph = {}

    for project in projects:
        project_graph[project] = []

    for pairs in dependencies:
        project_graph[pairs[0]].extend(pairs[1])
    return project_graph

projects = ['A', 'B', 'C', 'D', 'E', 'F']
dependencies = [('A','D'), ('F', 'B'), ('B','D'), ('F','A'), ('D','C')]
print(create_graph(projects,dependencies))