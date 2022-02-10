import { Component, OnInit, ViewChild } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';
import { asLiteral } from '@angular/compiler/src/render3/view/util';
import { DatePipe } from '@angular/common'
import {
  ChartComponent,
  ApexAxisChartSeries,
  ApexChart,
  ApexXAxis,
  ApexDataLabels,
  ApexTitleSubtitle,
  ApexStroke,
  ApexGrid,
  ApexMarkers,
  ApexFill,
  ApexTooltip,
  ApexYAxis
} from "ng-apexcharts";
import { dataSeries } from "./data-series";


@Component({
  selector: 'dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  public series!: ApexAxisChartSeries;
  public chart!: ApexChart;
  public dataLabels!: ApexDataLabels;
  public markers!: ApexMarkers;
  public title!: ApexTitleSubtitle;
  public fill!: ApexFill;
  public yaxis!: ApexYAxis;
  public xaxis!: ApexXAxis;
  public tooltip!: ApexTooltip;
  
  predictionDate : Date | undefined;
  companyName : string | undefined;
  companyForm !: FormGroup;
  roleData !: any;

  showPredictionGraph : boolean = false;

  constructor(private router:Router,
    private formBuilder: FormBuilder) {
      
     }

     

  ngOnInit(): void {
    this.companyForm = this.formBuilder.group({
      companyName:['']
    })
    this.getCompanyList();
    this.initChartData();
  }

  public initChartData(): void {
    let ts2 = 1484418600000;
    let dates = [];
    for (let i = 0; i < 120; i++) {
      ts2 = ts2 + 86400000;
      dates.push([ts2, dataSeries[1][i].value]);
    }

    this.series = [
      {
        name: "XYZ MOTORS",
        data: dates
      }
    ];
   
    this.chart = {
      type: "area",
      stacked: false,
      height: 350,
      zoom: {
        type: "x",
        enabled: true,
        autoScaleYaxis: true
      },
      toolbar: {
        autoSelected: "zoom"
      }
    };
    this.dataLabels = {
      enabled: false
    };
    this.markers = {
      size: 0
    };
    this.title = {
      text: "Stock Price Movement",
      align: "left"
    };
    this.fill = {
      type: "gradient",
      gradient: {
        shadeIntensity: 1,
        inverseColors: false,
        opacityFrom: 0.5,
        opacityTo: 0,
        stops: [0, 90, 100]
      }
    };
    this.yaxis = {
      labels: {
        formatter: function(val) {
          return (val / 1000000).toFixed(0);
        }
      },
      title: {
        text: "Price"
      }
    };
    this.xaxis = {
      type: "datetime"
    };
    this.tooltip = {
      shared: false,
      y: {
        formatter: function(val) {
          return (val / 1000000).toFixed(0);
        }
      }
    };
  }

  onSubmit(){
    this.showPredictionGraph = true;
    this.ngOnInit();
  }

  getCompanyList(){
    this.roleData = ['Apple','FaceBook' , 'Google']
  }

  openNav() {
    let ref : any =  document.getElementById('mySidebar');
    ref.style.width = "250px";
    let ref1 : any =  document.getElementById('main')
    ref1.style.marginLeft = "250px";
  }

  closeNav() {
    let ref : any = document.getElementById("mySidebar");
    ref.style.width = "0";
    let ref1 : any =  document.getElementById("main");
    ref1.style.marginLeft= "0";
  }

  checkPrediction() {
    this.showPredictionGraph = true;
    this.ngOnInit();
  }

}
