- 정확도 중시, 치명적 실수 없애기
- 더 이상 잘 쓰는 프롬프트가 경쟁력이 아니다. 잘 작동하는 AI 에이전트/시스템을 설계해야 한다.
- 이제 에이전트는 차분하고 객관적인 시선으로 새 기술이 나오면 어떻게 쓸지 고려
- 이 시스템의 액터는 누군가?
- 어느정도의 아키텍쳐, 뭘 고민하면서 했는지, 핸들링을 어디까지 고민해봤는지
- ai 아키텍쳐라는 직무가 있음
- 강력한 모델 + 탄탄한 전략 -> 우수한 성능
- 검증 가능하냐? 비용은?

- model distillation 모델 증류모델
- agentic AI
  - 최소한의 인간 개입으로 스스로 계획/판단/실행하는 자율성의 척도
  - memory, planning, tool use, autonomous action

- augmented LLM
  - workflow : 코드가 경로를 통제 및 재현
  - agent : 모델이 런타임 흐름 결정
  - 캐시 구성 잘하기, cost 고려

- context engineering

- Harness Engineering
  - Production에서 신뢰할 수 있도록 Deterministic Environment 구축 ➔ 제어 시스템 ➔ HARNESS

- Inference, Reasoning
  - inference = 확률적으로 가장 가능성 높은 단어를 예측하는 과정, LLM에서는 inference 단계 ≠ 논리적 reasoning 단계, 일관된 수학적 추론을 수행하는데 한계가 있음
  - Reasoning
    - LLM이 단순한 암기나 패턴 응답이 아닌, 논리 구조를 따라가면 정답에 도달하는 과정

- Tools
  - built-in Toos
  - Custom Tools
  - tool calling

- ReAct Framework

- 참고. supervisor

- MCP (context, tools)
  - 연결 파편화 해소
  - 로직 분리
  - 표준 규격 통합
  - 보안 권한 제어 <- 최근 공격점
  - 참고. llm은 stateless(메모리없음) 기반

- Host-Client-Server

- Sequence Diagram

- tool calling vs MCP
  - 서비스 목적과 요구사항에 맞춰 강한 결합(Native)과 느슨한 결합(MCP) 중 적절한 아키텍처를 선택해야 함

- A2A protocol
  - MCP가 외부 도구와의 연결을 담당한다면, A2A는 에이전트 간 협업과 통신을 전담
  - qhdks, roqkdtjd, gydbftjd

- AI Agentic Workflow
  - 결과를 평가하고 스스로 개선하는 순환형 흐름(interative loop)

- design framework
  - goal plan execut reflect

- goal
  - 무엇이 달성되면 끝인지, 산출물이 아니라 업무 결과를 중심으로 정의
  - 품질 : 근거성, 충실성, 완결성, 일관성
  - ![alt text](image-1.png)

- pipeline, supervisor, Agent-as-Tool, Swarm

- VectorDB와 ChromaDB의 차이

        1. VectorDB
        Vector Database(벡터 데이터베이스)의 줄임말.
        Embedding으로 변환된 숫자 벡터를 저장하고 유사한 데이터를 검색하는 데이터베이스의 총칭.
        특정 제품이 아니라 데이터베이스의 한 종류를 의미.

        2. ChromaDB
        VectorDB를 구현한 실제 제품 중 하나.
        Python에서 쉽게 사용할 수 있어 RAG 기초 실습에 많이 활용.
        Embedding 벡터 저장, 유사도 검색, 메타데이터 관리 등의 기능 제공.

        3. 대표적인 VectorDB 제품
        ChromaDB: Python 기반 실습 및 간단한 RAG 구현에 편리.
        Qdrant: 벡터 검색, 메타데이터 필터링, 검색 서비스 구축에 활용.
        Milvus: 대규모 벡터 데이터 검색에 활용.
        Pinecone: 클라우드 기반 관리형 VectorDB 서비스.

        4. 동작 흐름
        사용자 질문 입력 → Embedding 모델이 질문을 숫자 벡터로 변환 → ChromaDB 또는 Qdrant에서 유사한 벡터 검색 → 관련 문서 반환 → LLM이 검색된 문서를 참고

        ChromaDB 자체가 LLM은 아니며, 일반적으로 Embedding 모델과 함께 사용합니다.

        VectorDB = 벡터를 저장하고 검색하는 데이터베이스의 종류.
        ChromaDB = VectorDB 제품 중 하나.
        Qdrant = ChromaDB와 같은 VectorDB 제품.
        Embedding = 텍스트 등을 숫자 벡터로 변환하는 과정.
        RAG = 검색한 외부 정보를 LLM에 전달해 답변을 생성하는 방식.

        RDBMS라는 개념 아래 MySQL과 PostgreSQL이 있는 것처럼, VectorDB라는 개념 아래 ChromaDB와 Qdrant가 있다고 이해하시면 됩니다.

        LangGraph

        LangGraph는 AI의 작업 흐름(Workflow)을 설계하고 제어하는 프레임워크입니다.
        AI가 어떤 작업을 먼저 수행하고, 다음에는 무엇을 할지, 결과가 잘못되었을 때 다시 실행할지 등을 관리하는 도구입니다.

        1. LangGraph는 왜 사용할까요?
        일반적인 LLM 실행 흐름은 간단합니다.
        사용자 질문 → LLM → 답변 출력

        하지만 실제 AI 서비스에서는 여러 작업을 수행하고, 결과에 따라 다음 행동을 결정해야 할 수 있습니다.

        예시: RAG 기반 AI 서비스
        사용자 질문 → 질문 분석 → 관련 문서 검색(RAG) → LLM 답변 생성 → 답변 품질 검사

        정확한 답변인가?
        YES → 최종 답변 출력
        NO → 다시 검색 → 답변 재생성

        이처럼 조건에 따라 실행 경로를 변경하거나 이전 단계로 돌아가는 흐름을 LangGraph로 구현할 수 있습니다.

        2. LangGraph의 주요 용어
        Node(노드): 하나의 작업을 수행하는 단계.
        Edge(엣지): 노드와 노드를 연결하는 실행 경로.
        State(상태): 작업 과정에서 공유하고 관리하는 데이터.
        Conditional Edge(조건부 엣지): 조건에 따라 다음 실행 경로를 결정.
        Checkpoint(체크포인트): 실행 상태를 저장하여 중단된 작업을 이어서 실행.
        Human-in-the-loop: AI 작업 중간에 사람이 검토하거나 승인하는 방식.

        3. LangChain, LangGraph, LangSmith, RAG 차이
        LangChain: LLM, Prompt, Tool, Retriever 등을 연결하여 AI 기능 구현.
        LangGraph: AI 작업의 순서, 조건 분기, 반복 실행, 상태 관리.
        LangSmith: AI 실행 과정을 추적(Tracing)하고 평가(Evaluation).
        RAG: 외부 문서를 검색(Retrieve)하여 LLM 답변 생성에 활용.

        4. LangGraph는 언제 사용할까요?
        여러 Agent가 협력하는 Multi-Agent 시스템.
        답변이 잘못되면 다시 검색하거나 생성하는 Agentic RAG.
        조건에 따라 다른 작업을 실행하는 Workflow.
        사람의 승인이나 검토가 필요한 AI 서비스.
        이전 실행 상태를 저장하고 이어서 처리해야 하는 서비스.
        LangChain = AI 기능을 구현하고 연결하는 도구.
        LangGraph = AI 작업 흐름을 설계하고 제어하는 도구.
        LangSmith = AI 실행 과정을 확인하고 평가하는 도구.
        RAG = 외부 지식을 검색하여 답변에 활용하는 기술.

        LangChain은 무엇을 실행할 것인가?
        LangGraph는 어떤 순서와 조건으로 실행할 것인가?
        LangSmith는 실제로 어떻게 실행되었는가?

        ※ LangChain에서도 Agent를 구현할 수 있으며, LangGraph는 복잡한 실행 흐름과 상태를 직접 제어해야 할 때 유용합니다.

# 궁금한점

- ai agent(시스템), agentic AI(패러다임) 차이
