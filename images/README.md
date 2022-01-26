```mermaid
graph TD;
    Docker --> CentOS;
    Docker --> Ubuntu;


    CentOS --> CentOS-PGPLOT;
    
    CentOS --> CentOS-CFITSIO;
    
    CentOS --> CentOS-PSRCAT;

    CentOS-PGPLOT --> CentOS-IPP;
    CentOS-PGPLOT --> CentOS-Tempo;
    CentOS-PGPLOT --> CentOS-Tempo2;
    
    CentOS-PGPLOT --> CentOS-PSRCHIVE;
    CentOS-Tempo2 --> CentOS-PSRCHIVE;
    CentOS-PSRCAT --> CentOS-PSRCHIVE;

    CentOS-IPP --> CentOS-MPICH;
    CentOS-MPICH --> CentOS-DiFX;
    CentOS-Tempo --> CentOS-Presto;

    Ubuntu --> Ubuntu-PGPLOT;
    
    Ubuntu --> Ubuntu-CFITSIO;
    
    Ubuntu --> Ubuntu-PSRCAT;

    Ubuntu-PGPLOT -.-> Ubuntu-IPP;
    Ubuntu-PGPLOT --> Ubuntu-SD;
    Ubuntu-PGPLOT --> Ubuntu-Tempo;
    Ubuntu-PGPLOT --> Ubuntu-Tempo2;
    
    Ubuntu-PGPLOT --> Ubuntu-PSRCHIVE;
    Ubuntu-Tempo2 --> Ubuntu-PSRCHIVE;
    Ubuntu-PSRCAT --> Ubuntu-PSRCHIVE;

    Ubuntu-IPP --> Ubuntu-DiFX;
    Ubuntu-Tempo --> Ubuntu-Presto;

    CentOS -.-> SFXC;
    Ubuntu -.-> SFXC;
    CentOS -.-> Tempo2;
    Ubuntu -.-> Tempo2;
    CentOS-PGPLOT -.-> CentOS-Difmap;
    Ubuntu-PGPLOT -.-> Ubuntu-Difmap;
    CentOS -.-> dspsr;
    Ubuntu -.-> dspsr;
    CentOS -.-> psrchive;
    Ubuntu -.-> psrchive;
    CentOS -.-> Sigproc;
    Ubuntu -.-> Sigproc;

%% The color status  %%
    style Docker fill:#0f0,stroke:#333,stroke-width:4px;

    style CentOS fill:#0f0,stroke:#333,stroke-width:4px;
    style CentOS-PGPLOT fill:#0f0,stroke:#333,stroke-width:4px;
    style CentOS-CFITSIO fill:#0f0,stroke:#333,stroke-width:4px;
    style CentOS-PSRCAT fill:#0f0,stroke:#333,stroke-width:4px;
    style CentOS-IPP fill:#0f0,stroke:#333,stroke-width:4px;
    style CentOS-MPICH fill:#0f0,stroke:#333,stroke-width:4px;
    style CentOS-DiFX fill:#0f0,stroke:#333,stroke-width:4px;
    style CentOS-Tempo fill:#0f0,stroke:#333,stroke-width:4px;
    %%style CentOS-Tempo2 fill:#0f0,stroke:#333,stroke-width:4px;
    style CentOS-Presto fill:#0f0,stroke:#333,stroke-width:4px;

    style Ubuntu fill:#0f0,stroke:#333,stroke-width:4px;
    style Ubuntu-PGPLOT fill:#0f0,stroke:#333,stroke-width:4px;
    style Ubuntu-CFITSIO fill:#0f0,stroke:#333,stroke-width:4px;
    style Ubuntu-PSRCAT fill:#0f0,stroke:#333,stroke-width:4px;
    style Ubuntu-SD fill:#0f0,stroke:#333,stroke-width:4px;
    style Ubuntu-Tempo fill:#0f0,stroke:#333,stroke-width:4px;
    style Ubuntu-Tempo2 fill:#0f0,stroke:#333,stroke-width:4px;
    style Ubuntu-Presto fill:#0f0,stroke:#333,stroke-width:4px;


    subgraph STATUS
    DONE
    TBC
    style DONE fill:#0f0,stroke:#333,stroke-width:4px;
    style TBC fill:#ccf,stroke:#333,stroke-width:1px;
    end
```

